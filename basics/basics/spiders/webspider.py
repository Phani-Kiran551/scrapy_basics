from pydoc import source_synopsis
import scrapy, logging
class webspider(scrapy.Spider):
    name = 'web'

    start_urls = ['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']

    def parse(self, response):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        for products in response.css('div.product-item-info'):
            try:
                yield {
                    'name': products.css('a.product-item-link::text').get(),
                    'price': products.css('span.price::text').get().replace('£',''),
                    'tag': products.xpath('//div[@class="ribbon ribbon-exclusive"]/span/text()').get()
                    
                }
            except:
                yield {
                    'name': products.css('a.product-item-link::text').get(),
                    'price': 'sold out',
                    'tag': 'no tag',
                }
        logger.info("returns all the scraped data selected in an e-commerce website.")