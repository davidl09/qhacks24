from bs4 import BeautifulSoup
import requests

__urls = [
    "https://www.google.com/search?q={{TICKER}}",
    "https://www.reddit.com/r/investing/search?q={{TICKER}}&restrict_sr=1",  # Reddit search in subreddit
    "https://www.reddit.com/r/stocks/search?q={{TICKER}}&restrict_sr=1",  # Reddit search in subreddit
    "https://www.reddit.com/r/wallstreetbets/search?q={{TICKER}}&restrict_sr=1",  # Reddit search in subreddit
    "https://stocktwits.com/search?q={{TICKER}}",  # Assumed default for Stocktwits
    "https://www.investorvillage.com/smbd.asp?mb=2234&mn=56584&pt=msg&mid=19878568",  # No direct search, default not applicable
    "https://elite.finviz.com/search.ashx?p={{TICKER}}",  # Finviz search
    "https://www.valueinvestorsclub.com/value2/search/?q={{TICKER}}&stype=1",  # Assumed default for ValueInvestorsClub
    "https://www.theinvestorspodcast.com/community/search?q={{TICKER}}",  # Assumed default for TheInvestorsPodcast
    "https://www.morningstar.com/search?query={{TICKER}}",  # Assumed default for Morningstar
    "https://www.city-data.com/forum/search.php?search={{TICKER}}",  # City-data forum search
    "https://twitter.com/search?q={{TICKER}}&src=typed_query",  # Twitter search
    "https://www.linkedin.com/search/results/all/?keywords={{TICKER}}",  # LinkedIn search
    "https://www.facebook.com/search/top?q={{TICKER}}",  # Facebook search
    "https://www.instagram.com/explore/tags/{{TICKER}}/",  # Instagram tag search
    "https://www.tiktok.com/tag/{{TICKER}}",  # TikTok tag search
    "https://www.bloomberg.com/search?query={{TICKER}}",  # Assumed default for Bloomberg
    "https://www.cnbc.com/search/?query={{TICKER}}&qsearchterm={{TICKER}}",  # CNBC search
    "https://www.ft.com/search?q={{TICKER}}",  # Financial Times search
    "https://www.wsj.com/search/term.html?KEYWORDS={{TICKER}}",  # Wall Street Journal search
    "https://www.reuters.com/search/news?blob={{TICKER}}",  # Reuters search
    "https://seekingalpha.com/search?q={{TICKER}}",  # Seeking Alpha search
    "https://www.marketwatch.com/search?q={{TICKER}}",  # MarketWatch search
    "https://www.investing.com/search/?q={{TICKER}}",  # Investing.com search
    "https://finance.yahoo.com/search?q={{TICKER}}",  # Yahoo Finance search
    "https://www.businessinsider.com/sai?search={{TICKER}}",  # Assumed default for Business Insider
    "https://www.zerohedge.com/search-content?search_api_views_fulltext={{TICKER}}",  # ZeroHedge search
    "https://www.alphaarchitect.com/?s={{TICKER}}",  # Alpha Architect search
    "https://www.calculatedriskblog.com/search?q={{TICKER}}",  # Calculated Risk search
    "https://www.economist.com/search?q={{TICKER}}",  # Economist search
    "https://www.kitco.com/search_results.html?q={{TICKER}}",  # Kitco search
    "https://www.macroaxis.com/invest/search/{{TICKER}}",  # Macroaxis search
    "https://aswathdamodaran.blogspot.com/search?q={{TICKER}}",  # Aswath Damodaran's blog search
    "https://www.thebalance.com/search?q={{TICKER}}",  # The Balance search
    "https://www.investopedia.com/search?q={{TICKER}}",  # Investopedia search
    "https://www.nerdwallet.com/search?q={{TICKER}}",  # Nerdwallet search
    "https://www.tradingview.com/search/?q={{TICKER}}",  # TradingView search
    "https://stockcharts.com/cgi-bin/scans/search.pl?searchtext={{TICKER}}",  # StockCharts search
    "https://www.incrediblecharts.com/search/search.php?cx=partner-pub-"
    "7873262025927718%3A5074628558&cof=FORID%3A10&ie=ISO-8859-1&q={{TICKER}}&sa=Search",  # Incredible Charts search
    "https://www.barchart.com/search?query={{TICKER}}",  # Barchart search
    "https://finviz.com/search.ashx?p={{TICKER}}",  # Finviz search
    "https://www.motleyfool.com/search/?q={{TICKER}}",  # Motley Fool search
    "https://www.gurufocus.com/search/?q={{TICKER}}&search_symbol={{TICKER}}",  # GuruFocus search
    "https://simplywall.st/search?q={{TICKER}}",  # Simply Wall St search
    "https://www.estimize.com/searches?query={{TICKER}}",  # Estimize search
    "https://www.tipranks.com/search?tickers={{TICKER}}",  # TipRanks search
    "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={{TICKER}}",  # SEC EDGAR search
    "https://www.federalreserve.gov/search?q={{TICKER}}",  # Federal Reserve search
    "https://www.euronext.com/en/search/site/{{TICKER}}",  # Euronext search
    "https://www.londonstockexchange.com/search-results?k={{TICKER}}",  # London Stock Exchange search
    "https://www.hkex.com.hk/eng/search/search.aspx?q={{TICKER}}",  # HKEX search
]


def googlesearch_news(keyword: str):
    newsSearchURL = "https://www.google.com/search?q={{TICKER}}&tbm=nws".replace("{{TICKER}}", keyword)
    response = requests.get(newsSearchURL)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')




def scrape_for_keyword(url, keyword):
    search_suffix = "/search?q="  # This might need to be customized per site
    try:
        search_url = url.replace("{{TICKER}}", keyword)  # Construct search URL
        response = requests.get(search_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        text_with_keyword = [text for text in soup.stripped_strings if keyword.lower() in text.lower()]

        print("Request succeeded: " + search_url)
        return text_with_keyword
    except requests.RequestException as e:
        print(f"Request failed: {e}, URL: {search_url}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def get_content(ticker: str):
    result = {}
    for url in __urls:
        result[url] = scrape_for_keyword(url, ticker)
        if (len(result[url])) == 0:
            result[url].clear()
    return result


if __name__ == "__main__":
    print(get_content("TSLA"))