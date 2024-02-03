from pprint import pprint
from flask import Flask, render_template, request, redirect
import datetime
import sentimentAnalysis
import json
import yfinance as yf
import asyncio


app = Flask(__name__, static_folder='static', static_url_path='/')


@app.route('/')
def home():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


@app.route('/sentiment', methods=['GET'])
def sentiment():
    if request.method == 'GET':
        text = request.args.get('text')
        t = sentimentAnalysis.newsSentimentAPI.get_sentiment_articles(text)
        return str(t)





if __name__ == "__main__":
    app.run(debug=True, port=8080)
