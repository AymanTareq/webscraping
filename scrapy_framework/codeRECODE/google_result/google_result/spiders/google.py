import scrapy
import pandas as pd

class GoogleSpider(scrapy.Spider):
    name = 'google'
    # start_urls = ['https://www.google.com/travel/hotels/Greater%20Manchester/entity/ChcIke6cuObQ2qlLGgsvZy8xdGZwemNyOBAB?g2lb=2502548%2C2503781%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371335%2C4401769%2C4419364%2C4463666%2C4466981%2C4482194%2C4482438%2C4486153%2C4491350%2C4495816%2C4496891%2C4503421%2C4507899%2C4270859%2C4284970%2C4291517&hl=en-BD&gl=bd&ap=EgRDTmdCMANoAA&rp=OAFAAEgC&ictx=1&sa=X&utm_campaign=sharing&utm_medium=link&utm_source=htls&ts=CAESABpdCj8SOzIlMHg0ODdiYTY1NGQzODgyZWIxOjB4MmNjN2Q4MjIyMWM2ODA4MToSR3JlYXRlciBNYW5jaGVzdGVyGgASGhIUCgcI5Q8QAxgJEgcI5Q8QAxgKGAEyAggCKg8KCygBSgIgAToDQkRUGgA&ved=0CAAQ5JsGahcKEwjguv2-v_vuAhUAAAAAHQAAAAAQAg']
    def start_requests(self):
        df = pd.read_excel('hotel.xlsx','data')
        links = df['source link'].values.tolist()
        for link in links:
            if link is None:
                continue

            if not type(link) == type(''):
                continue
            yield scrapy.Request(link)

    def parse(self, response):
        # print("hello")
        phone = response.css('.AQSwS+ .CFH2De ::text').get()
        f_add = response.css('.K4nuhf .CFH2De:nth-child(1) ::text').get()
        f_add_lst = f_add.split(',')
        address1 = f_add_lst[0]
        if len(f_add_lst) > 3:
            address2 = f_add_lst[1]
        else:
            address2 = ''
        town_zip = f_add_lst[-2]
        town_country = town_zip.split(' ')[1]
        zip_lst = town_zip.split(' ')[-2:]
        zip_code = ' '.join(zip_lst)
        title = response.css('.fZscne ::text').get()
        location = response.css('.hAP9Pd:nth-child(5) span ::text').get()
        rating = response.css('.RZOZe ::text').get()
        yield {
          'Location': location.strip(),
          'Business name': title.strip(),
          'Star Rating': rating,
          'Address1': address1.strip(),
          'Address2': address2.strip(),
          'Town Country': town_country.strip(),
          'Zipcode': zip_code.strip(),
          'Phone': phone,
          'Source URL': response.url,
        }
