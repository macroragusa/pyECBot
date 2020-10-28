import sys
import scraper
import concurrent.futures

def main(links):
    results = {}

    if len(links) > 1:
        # Execute the scraping calling ecommerce_switcher and using multithreading
        with concurrent.futures.ThreadPoolExecutor() as executor:
            ebay_results = executor.map(scraper.ecommerce_switcher, links[1:])

        for result in ebay_results:
            results.update(result)

        for key, value in results.items():
            print(key, value)

    else:
        print("No element")
        sys.exit(0)


if __name__ == '__main__':
    main(sys.argv)
