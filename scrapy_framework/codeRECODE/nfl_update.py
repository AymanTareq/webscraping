import scrapy
from scrapy import Request
import re

def cleanup(input_string):
    # reomve \n, \t, \r @ and trailing space
    if input_string:
        return re.sub(r'[\n\r\t@]','',input_string).strip()




class NflSpider(scrapy.Spider):
    name = 'nfl'
    start_urls = ['https://www.nfl.com/players/']

    def parse(self, response):
        search_player_name = response.css('.d3-o-tabs__list-item+ .d3-o-tabs__list-item a::attr(href)').getall()[:3]
        for item in search_player_name:
            link = response.urljoin(item)
            yield Request(url=link,callback=self.player_list)
    
    def player_list(self,response):

        all_players = response.css('.nfl-o-cta--link::attr(href)').getall()[:4]

        for player in all_players:
            link = response.urljoin(player)
            yield Request(url=link, callback=self.parse_profile)

        # to do pagination task
        # next_page_url = response.css('a:contains("Next") ::attr(href)').get()
        # if next_page_url:
        #     next_page_url = response.urljoin(next_page_url)
        #     yield Request(url=next_page_url, callback=self.player_list)


    def parse_profile(self,response):
        height = response.css('.nfl-c-player-info__physical-data .d3-o-list__item:nth-child(1) .nfl-c-player-info__value::text').get()
        age = response.css('.nfl-c-player-info__career-data .d3-o-list__item:nth-child(3) .nfl-c-player-info__value::text').get()
        weight = response.css('.nfl-c-player-info__physical-data .d3-o-list__item:nth-child(2) .nfl-c-player-info__value::text').get()
        # player_info = {
        #     'height': height,
        #     'weight': weight,
        #     'age': age,
        # }
        link = response.css('.active+ li a::attr(href)').get()
        stats_link = response.urljoin(link)
        yield Request(url=stats_link, callback=self.parse_profile_summary,cb_kwargs=dict(weight=weight))

    def parse_profile_summary(self,response,weight):
        link = response.css('li:nth-child(3) .nfl-o-cta--secondary::attr(href)').get()
        link_logs = response.urljoin(link)
        weight=weight
        yield Request(url=link_logs,callback=self.parse_logs, cb_kwargs=dict(weight=weight))

    def parse_logs(self,response,weight):
        player_name = response.css('.nfl-c-player-header__title::text').get()
        player_weight = weight
        # process each table one by one
        all_table = response.css('table')
        for table in all_table:
            if all_table.index(table) == 0:
                season = response.css('.d3-l-grid--inner:nth-child(1) .d3-o-section-sub-title::text').get()
            elif all_table.index(table) == 1:
                season = response.css('.d3-l-grid--inner+ .d3-l-grid--inner .d3-o-section-sub-title::text').get()
            else:
                season = ''
            # process each row
            for row in table.css('tbody > tr'):
                # wk = row.css('th:nth-child(1)::text').get()
                # Game_date = row.css('th:nth-child(2)::text').get()
                # OPP = row.css('th:nth-child(3)::text').get()
                # Result = row.css('th:nth-child(4)::text').get()
                # AST = row.css('th:nth-child(7)::text').get()
                # PDEF = row.css('th:nth-child(10)::text').get()
                if season == '':
                    continue
                
                item = {
                    'player_name':cleanup(player_name),
                    'player_weight': player_weight,
                    'season':cleanup(season),                    
                    'wk': cleanup(row.css('td:nth-child(1)::text').get()),
                    'Game_date': cleanup(row.css('td:nth-child(2)::text').get()),
                    'OPP': cleanup(row.css('td:nth-child(3)::text').get()),
                    'Result': cleanup(row.css('td:nth-child(4)::text').get()),
                    'AST': cleanup(row.css('td:nth-child(7)::text').get()),
                    'PDEF': cleanup(row.css('td:nth-child(10)::text').get()),
                    'page_url': response.url,

                }

                yield item