from newsapi import NewsApiClient
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json

nltk.download('vader_lexicon')

analyser = SentimentIntensityAnalyzer()


def sentiment_analysis(text: str) -> dict:
    return analyser.polarity_scores(text)


def load_json_file(file_path) -> dict:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


class NewsApiScraper:
    def __init__(self):
        self.keys = load_json_file("apikeys.json")
        self.api = NewsApiClient(api_key=self.keys["newsapi"])

    def get_articles(self, ticker_symbol: str) -> list:
        articles = self.api.get_everything(ticker_symbol)
        result = []
        if articles["status"] != "ok":
            raise ConnectionAbortedError("NewsApi return status " + articles["status"])

        for article in articles["articles"]:
            tempDict = {}
            for key in ["title", "description", "content"]:
                tempDict[key] = article[key]
            result.append(tempDict)

        return result

    async def get_sentiment_articles(self, ticker_symbol: str) -> [float]:
        articles = self.get_articles(ticker_symbol)
        sentiments = {"neg": [], "neu": [], "pos": [], "com": []}
        for article in articles:
            temp = sentiment_analysis(article['content'])
            sentiments["com"].append(temp['compound'])
            sentiments["pos"].append(temp['pos'])
            sentiments["neg"].append(temp['neg'])
            sentiments["neu"].append(temp['neu'])

        for key, value in sentiments.items():
            sentiments[key] = sum(value) / len(value)

        return sentiments


newsSentimentAPI = NewsApiScraper()


if __name__ == "__main__":
    print(analyser.polarity_scores(""))
