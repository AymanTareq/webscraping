from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys

url = "https://www.brainyquote.com/"

# absolute path
chrome_driver_path = "/home/tareq/Desktop/webscraping/selenium/MahmudAhsan/chromedriver_linux64/chromedriver"

chrome_options = Options()
chrome_options.add_argument("--headless")

webdriver = webdriver.Chrome(
    executable_path=chrome_driver_path,
    options=chrome_options,
)

# default search query
search_query = "life"

if (len(sys.argv) >= 2):
    search_query = sys.argv[1]
    print(search_query)

with webdriver as driver:
    # timeout
    wait = WebDriverWait(driver,10)

    # retrieve data
    driver.get(url)

    # find search box
    search = driver.find_element_by_id("hmSearch")
    search.send_keys(search_query + Keys.RETURN)

    # wait
    wait.until(presence_of_element_located((By.ID,"quotesList")))

    # result 
    results = driver.find_elements_by_class_name("m-brick")
    # print(len(results))
    for quote in results:
        quoteArr = quote.text
        print(quoteArr)
        print()

    driver.close()
