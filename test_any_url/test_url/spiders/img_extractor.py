import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ImgExtractorSpider(CrawlSpider):
    name = 'img_extractor'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        all_img = response.xpath('//img/@src').getall()
        
        for img in all_img:
            yield {
                'src': response.urljoin(img),
                'url' : response.url,
            } 

