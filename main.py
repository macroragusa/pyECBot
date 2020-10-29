import sys
import scraper
import concurrent.futures

def ecommerce_switcher(link):
    """
    this function was created to be called for threading
    :param link: String - link of auction
    :return: Dictionary - the auction price of each supported site
    """
    result = {}
    if "ebay" in link.split("/")[2]:
        ebay = scraper.EbayScraper()
        ebay.do_scraping(link)
        result.update(ebay.get_prices())

    return result

def main(links):
    results = {}

    if len(links) > 1:
        # Execute the scraping calling ecommerce_switcher and using multithreading
        with concurrent.futures.ThreadPoolExecutor() as executor:
            ebay_results = executor.map(ecommerce_switcher, links[1:])

        for result in ebay_results:
            results.update(result)

        for key, value in results.items():
            print(key, value)

    else:
        print("No element")
        sys.exit(0)


if __name__ == '__main__':
    main(sys.argv)
