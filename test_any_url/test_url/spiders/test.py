import scrapy
from scrapy.shell import inspect_response

base_url = 'https://www.kickstarter.com/discover/advanced?woe_id=23424975&sort=magic&seed=2698351&page={}'
current_page = 2
class TestSpider(scrapy.Spider):
    global current_page
    name = 'test'
    # allowed_domains = ['kk']
    # print('current page before start_ulrs', current_page)
    start_urls = [
        # 'https://www.kickstarter.com/discover/advanced?woe_id=23424975&sort=magic&seed=2698351&page=1',
        # 'https://www.kickstarter.com/discover/advanced?google_chrome_workaround&woe_id=23424975&sort=magic&seed=2698351&page=1',
        base_url.format(current_page),
    ]

    def parse(self, response):
        # inspect_response(response, self)
        global current_page
        data = response.json()
        has_more = data["has_more"]

        for p in data["projects"]:
            name = p["name"]
            category = p["category"]["name"]
            creator = p["creator"]["name"]
            url = p["urls"]["web"]["project"]
            yield {
                'Name': name,
                'Category' : category,
                'Creator' : creator,
                'URL' : url,
            }
        # inspect_response(response,self)
        # print('Current_page before has more',current_page)
        if has_more:
            # print('Current_page after has more',current_page)
            next_page_url = base_url.format(current_page+1)
            # print('Current_page after next_page_url',current_page)
            yield scrapy.Request(next_page_url,callback=self.parse)
            # print('Current_page after yield',current_page)
            current_page = current_page + 1
            # print("current page after increment",current_page)


