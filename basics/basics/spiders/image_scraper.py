import scrapy, logging

class ImageSpider(scrapy.Spider):
    name = 'paris'
    start_urls = ['https://en.wikipedia.org/wiki/London_Bridge']

    def parse(self, response):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        raw_image_urls = response.css('.image img ::attr(src)').getall()
        clean_image_urls=[]
        for img_url in raw_image_urls:
            clean_image_urls.append(response.urljoin(img_url))
        
        yield {
            'image_urls': clean_image_urls
        }
        logger.info("Returns all the scraped images from the website.")
    
