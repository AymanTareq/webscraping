import scrapy


class CRateSpider(scrapy.Spider):
    name = 'c_rate'
    allowed_domains = ['https://www.bb.org.bd/econdata/exchangerate.php']
    start_urls = ['http://https://www.bb.org.bd/econdata/exchangerate.php/']

    def parse(self, response):
        pass
