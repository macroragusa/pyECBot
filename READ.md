# pyECBot
A simple bot to control the prices of products on the most famous e-commerce portals

### TODO
 - add multithreading to the method do_scraping in EbayScraper
   - main thread contains a FIFO for every keys of the dict prices and send results to (sqlite or  Django?)
   - the scrapings threads to add updated info in main threads