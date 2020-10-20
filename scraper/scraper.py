import bs4
import requests

class Scraper:

    def __init__(self):
        self.links = []
        self.prices = {}
        self.check_timeout = ""

    def add_link(self, link=None):
        if link is not None:
            self.links.append(link)

    def set_check_timeout(self, check_timeout=None):
        if check_timeout is not None:
            self.check_timeout = check_timeout

    def get_prices(self):
        return self.prices

    def get_links(self):
        return self.links

class EbayScraper(Scraper):

    def __init__(self):
        super().__init__()

    def do_scraping(self, links=None):
        """
        Return the price of the auctions of eEay
        :return: List - the price of the auctions
        """

        if links is not None:
            self.links = links

        for link in self.links:
            web_page = requests.get(link)
            web_page.raise_for_status()
            scraping = bs4.BeautifulSoup(web_page.text, 'html.parser')

            prcIsum = None
            prcIsum_bidPrice = None

            for attr in scraping.findAll("span", {"id": "prcIsum"}):
                prcIsum = attr.get("content")
            for attr in scraping.findAll("span", {"id": "prcIsum_bidPrice"}):
                prcIsum_bidPrice = attr.get("content")
            self.prices.update({link: float(prcIsum if prcIsum is not None else prcIsum_bidPrice)})

        return self.prices
