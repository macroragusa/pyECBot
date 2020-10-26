import bs4
import requests
import threading

class Scraper(threading.Thread):

    def __init__(self):
        self.exc = None
        self.link = ""
        self.prices = {}
        self.check_timeout = ""
        threading.Thread.__init__(self)

    def set_link(self, link=None):
        if link is not None:
            self.link = link

    def set_check_timeout(self, check_timeout=None):
        if check_timeout is not None:
            self.check_timeout = check_timeout

    def get_prices(self):
        return self.prices

    def get_link(self):
        return self.link

    def join(self):
        threading.Thread.join(self)
        # Since join() returns in caller thread we re-raise the caught exception if any was caught
        if self.exc:
            raise self.exc

class EbayScraper(Scraper):

    def __init__(self):
        super().__init__()

    def run(self):
        """
        Return the price of the auctions of eEay
        :return: List - the price of the auctions
        """

        web_page = requests.get(self.link)
        try:
            web_page.raise_for_status()
            scraping = bs4.BeautifulSoup(web_page.text, 'html.parser')
            prcIsum = None
            prcIsum_bidPrice = None

            for attr in scraping.findAll("span", {"id": "prcIsum"}):
                prcIsum = attr.get("content")
            for attr in scraping.findAll("span", {"id": "prcIsum_bidPrice"}):
                prcIsum_bidPrice = attr.get("content")
            self.prices.update({self.link: float(prcIsum if prcIsum is not None else prcIsum_bidPrice)})

        except Exception as e:
            self.exc = e
