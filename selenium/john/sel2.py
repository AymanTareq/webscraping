from selenium import webdriver
import pandas as pd



url = 'https://www.youtube.com/c/CodeRECODE/videos?view=0&sort=p&flow=grid'

driver_path = '/home/tareq/Desktop/webscraping/selenium/MahmudAhsan/chromedriver_linux64/chromedriver'

driver = webdriver.Chrome(driver_path)
driver.get(url)


# videos = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
videos = driver.find_elements_by_xpath('.//*[@id="details"]')

video_items = []
for video in videos:
    title = video.find_element_by_xpath('.//*[@id="video-title"]').text
    views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
    when = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text

    # print(title,views,when)
    vid_item = {
        'title':title,
        'views':views,
        'when':when
    }
    video_items.append(vid_item)

df = pd.DataFrame(video_items)
print(df)
# print(video_items)
# print(len(video_items))
driver.quit()
