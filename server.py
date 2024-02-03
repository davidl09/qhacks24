from pprint import pprint
from flask import Flask, render_template, request, redirect, url_for, session
import sentimentAnalysis
from os import environ as env
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv, find_dotenv
from urllib.parse import quote_plus, urlencode
import json


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

def login_required(route_function):
    def wrapper(*args, **kwargs):
        # Check if user is logged in
        if 'user' not in session:
            return redirect(url_for('login'))
        return route_function(*args, **kwargs)
    return wrapper


@app.route("/")
def home():
    return render_template("home.html", session=session.get('user'), pretty=json.dumps(session.get('user'), indent=4))


@app.route('/login')
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )


@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/dashboard.html")


@login_required
@app.route("/logout")
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


@login_required
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', session=session.get('user'), indent=4)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
