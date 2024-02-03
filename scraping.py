from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime

__urls = [
    "https://www.reddit.com/r/investing/",
    "https://www.reddit.com/r/stocks/",
    "https://www.reddit.com/r/wallstreetbets/",
    "https://stocktwits.com/",
    "https://www.investorvillage.com/",
    "https://elite.finviz.com/",
    "https://www.valueinvestorsclub.com/",
    "https://www.theinvestorspodcast.com/community/",
    "https://www.morningstar.com/forums",
    "https://www.city-data.com/forum/investing/",
    "https://twitter.com/ ",
    "https://www.linkedin.com/ ",
    "https://www.facebook.com/ ",
    "https://www.instagram.com/ ",
    "https://www.tiktok.com/ ",
    "https://www.bloomberg.com/markets/stocks",
    "https://www.cnbc.com/finance/",
    "https://www.ft.com/",
    "https://www.wsj.com/news/markets",
    "https://www.reuters.com/finance",
    "https://seekingalpha.com/",
    "https://www.marketwatch.com/",
    "https://www.investing.com/news/",
    "https://finance.yahoo.com/",
    "https://www.businessinsider.com/sai",
    "https://www.zerohedge.com/",
    "https://www.alphaarchitect.com/blog/",
    "https://www.calculatedriskblog.com/",
    "https://www.economist.com/finance-and-economics",
    "https://www.kitco.com/",
    "https://www.macroaxis.com/",
    "https://aswathdamodaran.blogspot.com/",
    "https://www.thebalance.com/investing-4074004",
    "https://www.investopedia.com/",
    "https://www.nerdwallet.com/blog/investing/",
    "https://www.tradingview.com/",
    "https://stockcharts.com/",
    "https://www.incrediblecharts.com/",
    "https://www.barchart.com/",
    "https://finviz.com/",
    "https://www.motleyfool.com/",
    "https://www.gurufocus.com/",
    "https://simplywall.st/",
    "https://www.estimize.com/",
    "https://www.tipranks.com/",
    "https://www.sec.gov/edgar/searchedgar/companysearch.html",
    "https://www.federalreserve.gov/",
    "https://www.euronext.com/en",
    "https://www.londonstockexchange.com/",
    "https://www.hkex.com.hk/",
]

urlReqResult = {}

for url in __urls:
    urlReqResult[url] = requests.get(url).content
    print(urlReqResult[url])

with open(f"{datetime.now()}_urls.txt", "w") as f:
    json.dump(urlReqResult, f)




