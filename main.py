import sys
import scraper


def main(links):
    """
    Main function
    :return: None
    """
    ebay = scraper.EbayScraper()
    if len(links) > 1:
        for link in links[1:]:
            ebay.add_link(link)
    else:
        print("No element")
    print(ebay.do_scraping())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv)
