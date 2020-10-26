import sys
import scraper


def main(links):
    """
    Main function
    :return: None
    """
    threads = []
    results = {}

    if len(links) > 1:
        for link in links[1:]:
            ebay_thread = scraper.EbayScraper()
            ebay_thread.set_link(link)
            ebay_thread.start()
            threads.append(ebay_thread)
    else:
        print("No element")
        sys.exit(0)

    for thread in threads:
        try:
            thread.join()
            results.update(thread.prices)
        except Exception as e:
            print(e)

    for key, value in results.items():
        print(key, value)

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv)
