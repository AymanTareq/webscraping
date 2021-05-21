import scrapy


class YelpSpider(scrapy.Spider):
    name = 'yelp'
    # allowed_domains = ['kk']
    start_urls = ['https://www.yelp.com/search?find_desc=Real%20Estate%20Companies&find_near=united-states-capitol-washington-3']

    def parse(self, response):
        # print("++++++++++++++++++++++++++")
        # print(response.url)
        # print(response.css('title ::text').get())
        # print(response.css('.css-1pxmz4g .css-166la90 ::text').getall())
        results = response.css('h4 a.css-166la90 ::attr(href)').getall()
        # print(results)
        # print(len(results))
        for result in results:
            link = response.urljoin(result)
            yield scrapy.Request(url=link,callback=self.profile)

        ## pagination
        next_page = response.css('a.next-link ::attr(href)').get()
        if next_page:
            print("Next tareq============",next_page)
            if not next_page.startswith('http'):
                print("We need to convert it info absolute link")
                next_page = response.urljoin(next_page)
                print('Inside if condition:::::',next_page)
                scrapy.Request(url=next_page, callback=self.parse)
            else:
                print('This is absolute link')
                scrapy.Request(next_page, callback=self.parse)
        else:
            print("==============================Next page link not found====================")

    def profile(self,response):
        # print('No ERROR!!!')
        # print(response.url)
        title = response.css('div > h1 ::text').get()
        type = response.css('.text-color--white__373c0__22aE8 .link-size--inherit__373c0__1VFlE ::text').get()
        web = response.css('.text--offscreen__373c0__2NIm_+ .text-size--large__373c0__3t60B .link-size--inherit__373c0__1VFlE ::text').get()
        if web is not None:
            web = 'www.'+web
        phone = response.css('.text--offscreen__373c0__2NIm_+ .text-size--large__373c0__3t60B ::text').getall()
        address_lst = response.css('address p ::text').getall()
        address = ''.join(address_lst)

        yield {
            'Title': title,
            'Category': type,
            'Phone': phone,
            'Website': web,
            'Address': address,
        }