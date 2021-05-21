import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DownloadsFilesItem

class EverythingSpider(CrawlSpider):
    name = 'everything'
    allowed_domains = ['python.org']
    start_urls = ['https://www.python.org/downloads/']

    rules = (
        Rule(LinkExtractor(restrict_css=r'.release-number a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        links = response.css('td:nth-child(1) a::attr(href)').getall()
        # print(links)
        item = DownloadsFilesItem()
        item['file_urls'] = links   # links must be list

        yield item
