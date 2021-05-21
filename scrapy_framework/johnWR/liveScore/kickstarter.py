from helium import *
from math import ceil
import time
import json

base_url = "https://www.kickstarter.com/discover/advanced?category_id=3&woe_id=23424975&sort=popularity&seed=2701020&page={}"

start_chrome("https://www.kickstarter.com/discover/advanced?category_id=3&woe_id=23424975&sort=popularity&seed=2701020&page=1")
time.sleep(3)

tot_item = int(find_all(S('//b[@class="count ksr-green-500"]'))[0].web_element.text.split()[0].replace(',',''))
max_page = ceil(tot_item / 12)

if max_page > 200:
    max_page = 200

# store output data
category_list = []
project_name_list = []
project_link_list = []
creator_list = []

# making dynamic url
for page in range(1,max_page+1):
    url = base_url.format(page)

    go_to(url)
    time.sleep(2)

    raw_data = [item.web_element.get_attribute('data-project') for item in find_all(S('//div[@data-project]'))]
    # now making raw_data to json data one by one.
    for data in raw_data:
        json_data = json.loads(data)

        # now parse the jsondata to extract information
        category = json_data['category']["name"]
        category_list.append(category)

        project_name = json_data['name']
        project_name_list.append(project_name)

        project_link = json_data['urls']['web']["project"]
        project_link_list.append(project_link)
        creator = json_data['creator']['name']
        creator_list.append(creator)

        print(category,'|', project_name,'|',creator,'|',project_link)

# now make a csv file
d = {
    'Category' : category_list,
    'Project Name' : project_name_list,
    'Project Link' : project_link_list,
    'Creator' : creator_list,
}

import pandas as pd
df = pd.DataFrame(d)
df.to_csv('output2.csv',index=False)

kill_browser()
print("Done!!")






