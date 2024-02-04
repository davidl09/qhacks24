import datetime
import json
import time
from pprint import pprint
from flask import Flask, render_template, request, redirect, url_for, session
import sentimentAnalysis
from os import environ as env
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv, find_dotenv
from urllib.parse import quote_plus, urlencode
import yfinance_best_worst

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__, static_folder='static', static_url_path='/', template_folder='templates')
app.secret_key = env['APP_SECRET_KEY']

oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)

bestworst_lastdate = datetime.datetime.now()

def login_required(route_function):
    def wrapper(*args, **kwargs):
        # Check if user is logged in
        if 'user' not in session:
            return redirect(url_for('login'))
        try:
            return route_function(*args, **kwargs)
        except ValueError:
            return redirect(url_for('login'))
    wrapper.__name__ = route_function.__name__
    return wrapper


@app.route("/")
def home():
    return render_template("homepage.html", session=session.get('user'), indent=4)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', session=session.get('user'), indent=4)


@app.route('/login')
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )


@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/dashboard")


@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )


@app.route('/sentiment', methods=['GET'])
def sentiment():
    if request.method == 'GET':
        text = request.args.get('text')
        t = sentimentAnalysis.newsSentimentAPI.get_sentiment_articles(text)
        return str(t)

@app.route('/bestworst')
def bestworst():
    if bestworst_lastdate.date().day != datetime.datetime.now().day:
        yfinance_best_worst.get_best_and_worst_performing_stocks.cache_clear()
    return json.dumps(yfinance_best_worst.get_best_and_worst_performing_stocks())


@app.route('/kevin')
@login_required
def kevin():
    return render_template('kevin-advisor.html', session=session.get('user'))


if __name__ == "__main__":
    app.run(debug=True, port=8080)
