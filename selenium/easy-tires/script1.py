from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver_path = '/home/tareq/Desktop/webscraping/selenium/MahmudAhsan/chromedriver_linux64/chromedriver'
url = 'https://www.tires-easy.com/tires/amp-tires'

driver = webdriver.Chrome(driver_path)
driver.get(url)

items = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "productListItem", " " ))]')

