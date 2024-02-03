import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

analyser = SentimentIntensityAnalyzer()


if __name__ == "__main__":
    print(analyser.polarity_scores(""))
