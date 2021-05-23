from requests_html import AsyncHTMLSession
import asyncio
import time
import pandas as pd
import numpy as np

df = pd.read_csv('/home/tareq/Desktop/fiverr/clients/Lawyer_data/lawyers_url.csv')

url_full_lst = df['urls'].tolist()
urls = url_full_lst[100:200]

data_lst = []
count = int(1)
url = ''
async def work(session, url):
    global count
    r = await session.get(url)
    print(f"---{r.status_code} | {count} item scraped! ---")
    response = r.html

    bn = response.xpath('//div[@class="sales-info"]/h1/text()', first=True)

    cats = response.xpath('//p[@class="cats"]/a/text()')

    try:
        cat1 = cats[0]
    except:
        cat1 = ''
    try:
        cat2 = cats[1]
    except:
        cat2 = ''
    try:
        cat3 = cats[2]
    except:
        cat3 = ''

    pn = response.xpath('//p[@class="phone"]/text()', first=True)
    ad = response.xpath('//h2[@class="address"]/span/text()', first=True)
    csz = response.xpath('//h2[@class="address"]/text()', first=True)

    try:
        c = csz.split(',')[0]
    except:
        c = ''
    try:
        s = csz.split(',')[1].strip().split(' ')[0]
    except:
        s = ''
    try:
        z = csz.split(',')[1].strip().split(' ')[1]
    except:
        z = ''

    w = response.xpath('//a[@class="primary-btn website-link"]/@href', first=True)
    try:
        e = response.xpath('//div[@class="business-card-footer"]/a[@class="email-business"]/@href', first=True)
        e = e.split(':')[1]
    except:
        try:
            e = response.xpath('//p/a[@class="email-business"]/@href', first=True)
            e = e.split(':')[1]
        except:
            e = ''

    d = {
        'Business Name' : bn,
        'Website' : w,
        'Email' : e,
        'Phone Number' : pn,
        'Address' : ad,
        'City' : c,
        'State' : s,
        'Postal' : z,
        'Category 1' : cat1,
        'Category 2' : cat2,
        'Category 3' : cat3,
        'URLs' : response.url,
    }
    data_lst.append(d)
    count += 1
    return

def output():
    df = pd.DataFrame(data_lst)
    df.to_csv('testing1.csv', index=False)
    print('Saved to csv file.')
    return


async def main(urls):
    session = AsyncHTMLSession()
    tasks = (work(session, url) for url in urls)
    return await asyncio.gather(*tasks)


start = time.perf_counter()
try:
    asyncio.run(main(urls))
except:
    end = time.perf_counter()
    time_taken = round(end - start, 3)
    print('---------------------------------------')
    print('Something Wrong. Scraped partially.')
    print(f'{len(data_lst)} items scraped. Last item index: {urls.index(url)}')
    output()
    print('Total Time Taken:', time_taken)
    import sys
    sys.exit()

end = time.perf_counter()
time_taken = round(end - start, 3)

print('---------------------------------------')
print(f'{len(data_lst)} items scraped!!!')

output()
print('Total Time Taken:', time_taken, 'sec')