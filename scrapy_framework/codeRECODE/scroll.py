from typing import Text
import scrapy

base = 'http://quotes.toscrape.com/api/quotes?page={}'
class ScrollSpider(scrapy.Spider):
    name = 'scroll'
    start_urls = [base.format(1)]

    def parse(self, response):
        data = response.json()          # scrapy 2.2
        # print(data['has_next'])
        # print(data['page'])
        for quote in data["quotes"]:
            yield {
                'Author' : quote["author"]["name"],
                'Quote': quote["text"]
            }
        current_page = data["page"]
        if data["has_next"]:
            next_page_url = base.format(current_page+1)
            yield scrapy.Request(next_page_url)
