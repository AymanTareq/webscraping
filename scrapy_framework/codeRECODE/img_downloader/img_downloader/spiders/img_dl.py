import scrapy


class ImgDlSpider(scrapy.Spider):
    name = 'img_dl'
    start_urls = [
        'https://www.jugantor.com/',
        ]

    def parse(self, response):
        img_urls =  response.css('.card-img.rounded-0.w-100.d-block::attr(src)').getall()
        
        yield {
            'image_urls': img_urls
        }


