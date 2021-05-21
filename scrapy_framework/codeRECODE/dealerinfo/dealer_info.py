import scrapy


class DealerInfoSpider(scrapy.Spider):
    name = 'dealer_info'
    start_urls = ['https://www.machinerypete.com/dealerships/search']

    def parse(self, response):
        states_link = response.css('.btn-xs ::attr(href)').getall()
        for link in states_link:
            link = response.urljoin(link)
            yield scrapy.Request(link,callback=self.dealers_in_a_state)
    
    def dealers_in_a_state(self,response):
        stores_link = response.css('.col-xs-6 ::attr(href)').getall()
        for link in stores_link:
            link = response.urljoin(link)
            yield scrapy.Request(link, callback=self.parse_single_store)
    
    def parse_single_store(self,response):
        title = response.css('#panel a+ a::text').get()
        contact = response.css('.col-xs-12:nth-child(2) .store-header+ .store-item::text').get()
        phone = response.css('.col-xs-12:nth-child(2) .store-item:nth-child(3) a::text').get()
        if phone is None:
            phone = response.css('.store-item > a::text').getall()[-1]
        email = response.css('.col-xs-12:nth-child(2) .store-item~ .store-item+ .store-item::text').get()
        website = response.css('.store-item:nth-child(2) a::text').get()
        a1 = response.css('.col-xs-12:nth-child(3) .store-header+ .store-item::text').get()
        a2 = response.css('.col-xs-12:nth-child(3) .store-item:nth-child(3)::text').get()
        address = a1 + a2
        h = response.css('.col-xs-12:nth-child(4) .store-item::text').getall()
        hours = '; '.join(h)
        yield {
            'Title': title,
            'Contact': contact,
            'Phone': phone,
            'Email': email,
            'Website': website,
            'Address': address,
            'Hours': hours,
            'URL': response.url
        }






