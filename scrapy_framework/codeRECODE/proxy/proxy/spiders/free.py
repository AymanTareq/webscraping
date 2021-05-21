import scrapy
from scrapy.shell import inspect_response


class FreeSpider(scrapy.Spider):
    name = 'free'

    def start_requests(self):
        for i in range(5):
            yield scrapy.Request(url='http://httpbin.org/ip',dont_filter=True)

    def parse(self,response):
        print(response.text)
