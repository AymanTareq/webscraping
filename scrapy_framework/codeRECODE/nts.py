import scrapy
import json

from scrapy.http import headers, request

class NtsSpider(scrapy.Spider):
    name = 'nts'
    start_urls = [
        'https://directory.ntschools.net/#/schools',
       ]
    headers = {
        'Accept':" application/json",
        'Accept':"Encoding: gzip, deflate, br",
        'Accept':"Language: en-US,en;q=0.9,bn;q=0.8",
        'Cache':"Control: no-cache",
        'Connection':" keep-alive",
        'Cookie':" BIGipServerdirectory.ntschools.net_443.app~directory.ntschools.net_443_pool=360972810.20480.0000",
        'Host':" directory.ntschools.net",
        'Pragma':" no-cache",
        'Referer':" https://directory.ntschools.net/",
        'Sec':"Fetch-Dest: empty",
        'Sec':"Fetch-Mode: cors",
        'Sec':"Fetch-Site: same-origin",
        'User':"Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        'X':"Requested-With: Fetch",
    }


    def parse(self, response):
        url = 'https://directory.ntschools.net/api/System/GetAllSchools'
        request = scrapy.Request(url,callback=self.parse_api,headers=self.headers)

        yield request

    def parse_api(self,response):
        base_url = 'https://directory.ntschools.net/api/System/GetSchool?itSchoolCode='
        raw_data = response.body
        data = json.loads(raw_data)
        for school in data:
            school_code = school['itSchoolCode']
            school_url = base_url+school_code
            request = scrapy.Request(
                school_url,
                callback=self.parse_school,
                headers=self.headers
            )
            yield request

    def parse_school(self,response):
        raw_data = response.body
        data = json.loads(raw_data)
        yield {
            'School_Name': data['name'],
            'Physical_Address': data['physicalAddress']['displayAddress'],
            'Postal_Address': data['postalAddress']['displayAddress'],
            'Email': data['mail'],
            'Phone' : data['telephoneNumber'],
            'SchoolMgt_Name': data['schoolManagement'][0]['lastName'],
            'Designation': data['schoolManagement'][0]['position'],
            'Mobile': data['schoolManagement'][0]['phone'],
            'Email_2': data['schoolManagement'][0]['email'],
        }