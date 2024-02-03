from flask import Flask, render_template
import datetime

app = Flask(__name__, static_folder='static', static_url_path='/')


@app.route('/')
def home():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
