import scrapy
from scrapy_splash import SplashRequest
import re

def cleanup(input_string):
    # reomve \n, \t, \r  and trailing space
    if input_string:
        return re.sub(r'[\n\r\t]','',input_string).strip()


class SssSpider(scrapy.Spider):
    name = 'sss'

    def start_requests(self):
        url = 'https://www.tires-easy.com/tires/'
        yield SplashRequest(
            url = url,
            callback=self.parse,
            args={'wait':5.0}
        )

    def parse(self, response):
        tire_links = response.css('h2 a::attr(href)').getall()
        for tire_link in tire_links:
            link = response.urljoin(tire_link)
            yield SplashRequest(url=link, callback=self.tire_profile,args={'wait':5.0})

        ## Handling Pagination
        tot_page = response.css('input#jNumberOfPages::attr(value)').get()
        next_page = 'https://www.tires-easy.com/tires/?page='
        limit = 2
        while limit <= int(tot_page):
            for page in range(2,int(tot_page)+1):
                next_page_link = next_page+str(page)
                yield SplashRequest(url=next_page_link,callback=self.parse,args={'wait':5.0})
                limit += 1

    def tire_profile(self,response):
        Brand = response.css('#breadcrumb li:nth-child(7) span::text').get()
        model = response.css('#breadcrumb li:nth-child(10) span::text').get()
        size = response.css('button#dropdown-menu-size-selector::text').get()
        price = response.css('.price.right.selection::text').get()
        sidewall = response.css('.product-specifications-table tbody tr:nth-child(2) td:nth-child(2)::text').get()
        Load_index = response.css('.product-specifications-table tbody tr:nth-child(3) td:nth-child(2)::text').get()
        Speed_rating = response.css('.product-specifications-table tbody tr:nth-child(4) td:nth-child(2)::text').get()
        Ply_Rating = response.css('.product-specifications-table tbody tr:nth-child(5) td:nth-child(2)::text').get()
        UTQG = response.css('.product-specifications-table tbody tr:nth-child(6) td:nth-child(2)::text').get()
        Max_single_load = response.css('.product-specifications-table tbody tr:nth-child(7) td:nth-child(2)::text').get()
        Max_single_air = response.css('.product-specifications-table tbody tr:nth-child(8) td:nth-child(2)::text').get()
        Tread_Depth = response.css('.product-specifications-table tbody tr:nth-child(9) td:nth-child(2)::text').get()
        Tread_design = response.css('.product-specifications-table tbody tr:nth-child(10) td:nth-child(2)::text').get()
        Rim_width_range = response.css('.product-specifications-table tbody tr:nth-child(11) td:nth-child(2)::text').get()
        Measured_Rim_width = response.css('.product-specifications-table tbody tr:nth-child(12) td:nth-child(2)::text').get()
        Section_width = response.css('.product-specifications-table tbody tr:nth-child(13) td:nth-child(2)::text').get()
        Tread_width = response.css('.product-specifications-table tbody tr:nth-child(14) td:nth-child(2)::text').get()
        overall_diameter = response.css('.product-specifications-table tbody tr:nth-child(15) td:nth-child(2)::text').get()
        Manufacturer = response.css('.product-specifications-table tbody tr:nth-child(16) td:nth-child(2)::text').get()

        yield {
            'Brand': cleanup(Brand),
            'Model': cleanup(model),
            'Size': cleanup(size),
            'Price': cleanup(price),
            'Sidewall': cleanup(sidewall),
            'Load Index': cleanup(Load_index),
            'Speed Rating': cleanup(Speed_rating),
            'Ply Rating': cleanup(Ply_Rating),
            'UTQG': cleanup(UTQG),
            'Max Single Load(lbs)': cleanup(Max_single_load),
            'Max Single Air Pressure(PSI)': cleanup(Max_single_air),
            'Tread Depth': cleanup(Tread_Depth),
            'Tread Design': cleanup(Tread_design),
            'Rim Width Range': cleanup(Rim_width_range),
            'Measured Rim Width': cleanup(Measured_Rim_width),
            'Section Width': cleanup(Section_width),
            'Tread Width': cleanup(Tread_width),
            'Overall Diameter': cleanup(overall_diameter),
            'Manufacturer #': cleanup(Manufacturer),
            'URL': response.url
            }