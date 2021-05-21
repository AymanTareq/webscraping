import scrapy
from ..items import AmazonScrapingItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    # allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011',
    # 'https://www.amazon.com/Books-Last-30-days/s?i=stripbooks&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&page=2&qid=1610595769&ref=sr_pg_2',
    ]

    def parse(self, response):
        items = AmazonScrapingItem()

        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
        clean_product_author = []
        for i in product_author:
            an = ''
            for j in i:
                if j != '\n':
                    an += j
            clean_product_author.append(an)
        # product_price = response.css('.a-spacing-top-small .a-price span span').css('::text').extract()
        product_price = response.css('.a-spacing-mini:nth-child(1) .a-text-price').css('::text').extract()
        clean_product_price = []
        for i in range(0,len(product_price),2):
            clean_product_price.append(product_price[i])
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = clean_product_author
        items['product_price'] = clean_product_price
        items['product_imagelink'] = product_imagelink

        yield items
        # yield{
        #     'Product_name': product_name,
        #     'product_author':clean_product_author,
        #     'product_price':clean_product_price,
        #     'product_imagelink':product_imagelink
        # }

        # next_page = 'https://www.amazon.com/Books-Last-30-days/s?i=stripbooks&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&page='+str(AmazonSpider.page_number)+'&qid=1610595769&ref=sr_pg_2'
        # if AmazonSpider.page_number <= 5:
        #     AmazonSpider.page_number += 1
        #     yield response.follow(next_page, callback=self.parse)
