import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksCrawlSpider(CrawlSpider):
    name = 'books_crawl'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/catalogue/category/books/fiction_10/index.html']

    rules = (
        Rule(LinkExtractor(restrict_css='h3 > a'), callback='parse_item', follow=False),
        Rule(LinkExtractor(restrict_css='.next > a'), follow=True),
        Rule(LinkExtractor(restrict_css='.nav-list ul a'), follow=True),
    )

    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        yield {
            'Title' : response.css('h1 ::text').get(),
            'Category': response.xpath('//ul[@class="breadcrumb"]/li[position()=3]/a/text()').get(),
            'Link' : response.url
        }