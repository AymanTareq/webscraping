import scrapy

class QtsSpider(scrapy.Spider):
    name = 'qts'
    # allowed_domains = ['quotes.toscrape.com/random']
    start_urls = [
    # 'http://quotes.toscrape.com/random',
    # 'https://en.wikipedia.org/wiki/Python_(programming_language)',
    'https://scrapeit.home.blog/',
    ]

    def parse(self, response):
        for article in response.css('article'):
            yield {
                'Article Heading': article.css('h2 a::text').get(),
                'First Para': article.css('p::text').get(),
                'Author': article.css('footer a::text').get(),
                'Date': article.css('footer time::text').get(),
                'Category tag': article.css('footer a[rel="category tag"]::text').getall(),
            }

        next_page = response.css('.next.page-numbers::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


########### Wikipedia table of content scraping ===========================
"""
class QtsSpider(scrapy.Spider):
    name = 'qts'
    # allowed_domains = ['quotes.toscrape.com/random']
    start_urls = [
    # 'http://quotes.toscrape.com/random',
    'https://en.wikipedia.org/wiki/Python_(programming_language)',
    ]

    def parse(self, response):
        for toc in response.css('.toclevel-1'):
            yield {
                'Sl no.': toc.css('.tocnumber::text').get(),
                'content': toc.css('.toctext::text').get()
            }

"""




# ## Basic Scraping
# class QtsSpider(scrapy.Spider):
#     name = 'qts'
#     # allowed_domains = ['quotes.toscrape.com/random']
#     start_urls = ['http://quotes.toscrape.com']

#     def parse(self, response):
#         # print(f"Got response from {response.url}")
#         self.log(f"Got response from {response.url}")
#         # print("hello========================^^^^^^^^**************")

#         item = {
#             'quote': response.css('[itemprop="text"]::text').get(),
#             'author': response.css('.author::text').get(),
#             'tags': response.css('.tag::text').getall()
#         }
#         yield item

