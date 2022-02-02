import imp
from jmespath import search
import scrapy
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
        # inspect_response(response, self)
        request.headers.get('Cookie').split(b';')[-1].decode().strip().replace(" ","")
        