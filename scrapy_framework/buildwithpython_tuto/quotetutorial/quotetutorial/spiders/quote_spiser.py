import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 1
    
    start_urls = [
        'http://quotes.toscrape.com/login',
    ]
    def parse(self,response):
        token = response.css('form input::attr(value)').extract_first()
        print(token)
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username':'aymantareqbd',
            'password':'ljfldjfdsj'
        },callback=self.start_scraping)

    def start_scraping(self,response):
        open_in_browser(response)
        items = QuotetutorialItem()
        
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            
            yield items

        # next_page = response.css('li.next a::attr(href)').get()
        next_page = 'http://quotes.toscrape.com/page/'+ str(QuoteSpider.page_number)+'/'

        # if next_page is not None:
        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number += 1
            yield response.follow(next_page,callback = self.start_scraping)
        
