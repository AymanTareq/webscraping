import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class H1SpiderSpider(CrawlSpider):
    name = 'h1_spider'
    allowed_domains = [
        # 'books.toscrape.com',
        'jugantor.com',
        ]
    start_urls = [
        # 'https://books.toscrape.com/',
        'https://www.jugantor.com/',
        ]

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        items = response.xpath('//h1/text()').getall()
        for i in items:
            yield {
                'text':i,
                'url':response.url,
            }
