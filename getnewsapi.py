from newsapi import NewsApiClient
import json
import sentimentAnalysis


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

    def get_sentiment_articles(self, ticker_symbol: str) -> [float]:
        articles = self.get_articles(ticker_symbol)
        sentiments = {"neg": [], "neu": [], "pos": [], "com": []}
        for article in articles:
            temp = sentimentAnalysis.sentiment_analysis(article['content'])
            sentiments["com"].append(temp['compound'])
            sentiments["pos"].append(temp['pos'])
            sentiments["neg"].append(temp['neg'])
            sentiments["neu"].append(temp['neu'])

        for key, value in sentiments.items():
            sentiments[key] = sum(value) / len(value)

        return sentiments


if __name__ == "__main__":
    # company_names = [
    #     "Apple Inc.",
    #     "Microsoft Corporation",
    #     "Alphabet Inc. (Google)",
    #     "Amazon.com Inc.",
    #     "Meta Platforms Inc. (Facebook)",
    #     "Tesla Inc.",
    #     "JPMorgan Chase & Co.",
    #     "Visa Inc.",
    #     "NVIDIA Corporation",
    #     "Johnson & Johnson",
    #     "Walmart Inc.",
    #     "Procter & Gamble Company",
    #     "Mastercard Incorporated",
    #     "PayPal Holdings Inc.",
    #     "UnitedHealth Group Incorporated",
    #     "Bank of America Corporation",
    #     "The Walt Disney Company",
    #     "Adobe Inc.",
    #     "The Home Depot Inc.",
    #     "Intel Corporation",
    #     "Salesforce.com Inc.",
    #     "Comcast Corporation",
    #     "Exxon Mobil Corporation",
    #     "Netflix Inc.",
    #     "AT&T Inc.",
    #     "Verizon Communications Inc.",
    #     "The Coca-Cola Company",
    #     "Abbott Laboratories",
    #     "Thermo Fisher Scientific Inc.",
    #     "NIKE Inc.",
    #     "Cisco Systems Inc.",
    #     "PepsiCo Inc.",
    #     "Costco Wholesale Corporation",
    #     "Merck & Co. Inc.",
    #     "Chevron Corporation",
    #     "United Parcel Service Inc.",
    #     "The Boeing Company",
    #     "Eli Lilly and Company",
    #     "International Business Machines Corporation (IBM)",
    #     "Accenture plc",
    #     "Medtronic plc",
    #     "Oracle Corporation",
    #     "QUALCOMM Incorporated",
    #     "Philip Morris International Inc.",
    #     "Honeywell International Inc.",
    #     "3M Company",
    #     "The Goldman Sachs Group Inc.",
    #     "U.S. Bancorp",
    #     "S&P Global Inc.",
    #     "American Express Company"
    # ]
    #
    # plt.figure(dpi=400)
    # sentiments = {}
    # sentimentapi = NewsApiScraper()
    # for company in company_names:
    #     sentiments[company] = sentimentapi.get_sentiment_articles(company)
    # for company, sentiment in sentiments.items():
    #     print(company, sentiment)

    analyser = NewsApiScraper()
    while True:
        keyword = input("Enter a keyword: \n")
        print("Analysing...")
        print("Sentiment of " + keyword + " is : " + str(analyser.get_sentiment_articles(keyword)))

