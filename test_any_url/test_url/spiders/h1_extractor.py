import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class H1ExtractorSpider(CrawlSpider):
    name = 'h1_extractor'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        all_h1 = response.xpath('//h1/text()').getall()
        
        for h1 in all_h1:
            yield {
                'text': h1,
                'url' : response.url,
            } 
