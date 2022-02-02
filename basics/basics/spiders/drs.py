import imp
from jmespath import search
import scrapy, logging
from scrapy.shell import inspect_response

class DrsSpider(scrapy.Spider):
    name = 'drs'
    url = 'https://drs.faa.gov/guest/login?targetUrl=/search'
    start_urls = [url]
    custom_settings = {
        'COOKIES_ENABLED':True,
        'COOKIES_DEBUG':True
    }
    
    def parse(self, response):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        # inspect_response(response, self)
        """Go to the terminal and run
        
        ```bash
        spider using scrapy crawl drs
        ```
        and paste this command in the interactive shell.
        
        ```bash
        request.headers.get('Cookie').split(b';')[-1].decode().strip().replace(" ","")
        ```
        """

        logger.info("starts a scrapy interactive shell by which when we type in the above commands will get us the cookies.")
        
        