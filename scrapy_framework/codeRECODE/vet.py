import scrapy


class VetSpider(scrapy.Spider):
    name = 'vet'
    start_urls = ['http://www.findalocalvet.com/Find-a-Veterinarian.aspx']

    def parse(self, response):
        major_cities = response.css('.itemresult a::attr(href)').getall()[:53]
        for link in major_cities:
            link = response.urljoin(link)
            yield scrapy.Request(link,callback=self.parse_cities)

    def parse_cities(self,response):
        all_vets = response.css('h3 a.fn.org::attr(href)').getall()
        for link in all_vets:
            link = response.urljoin(link)
            yield scrapy.Request(link, callback=self.parse_single_vet)
        
        next_page = response.css('a:contains("Next") ::attr(href)').get()
        if next_page:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(next_page_link, callback=self.parse_cities)
    
    def parse_single_vet(self,response):
        title = response.css('div h1::text').get()
        city = response.css('.locality::text').get()
        state = response.css('.region::text').get()
        phone = response.css('strong.tel::text').get()
        link = response.url

        yield {
            'Practice Name': title,
            'City': city,
            'State': state,
            'Phone': phone,
            'Link':link
        }




