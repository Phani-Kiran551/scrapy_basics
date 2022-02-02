import scrapy, logging


class MyprojectSpider(scrapy.Spider):
    name = "project"

   
    start_urls = [
        "https://en.wikipedia.org/wiki/London_Bridge"
   ]
    def parse(self, response):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        for sel in response.xpath('//ul/li'):
            try:
                    title = sel.xpath('a/text()').extract()
                    if title == "":
                        pass
                    else:
                        yield {
                            'title' : sel.xpath('a/text()').extract() 
                        }

            except:
                    pass
        logger.info(
            "Returns all the scraped unordered lists from the website."
        )
    
    
