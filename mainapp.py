from pprint import pprint
from flask import Flask, render_template, request, redirect
import datetime
import sentimentAnalysis
import json


app = Flask(__name__, static_folder='static', static_url_path='/')


@app.route('/')
def home():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


@app.route('/sentiment/<text>', methods=['GET'])
def sentiment(text):
    if request.method == 'GET':
        t = sentimentAnalysis.sentiment_analysis(text)
        return str(t)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
