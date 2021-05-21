import scrapy
from ..items import DownloadsFilesItem
from downloads_files import items

class FilesSpider(scrapy.Spider):
    name = 'file'
    # allowed_domains = ['kk']
    start_urls = ['https://www.python.org/downloads/release/python-380/']

    def parse(self, response):
        links = response.css('td:nth-child(1) a::attr(href)').getall()
        # print(links)
        item = DownloadsFilesItem()
        item['file_urls'] = links   # links must be list

        yield item
