from pprint import pprint

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

analyser = SentimentIntensityAnalyzer()


def sentiment_analysis(text: str) -> dict:
    return analyser.polarity_scores(text)


if __name__ == "__main__":
    print(analyser.polarity_scores(""))
