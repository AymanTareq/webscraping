# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait

# # url = 'http://the-internet.herokuapp.com/login'
# # url = 'http://the-internet.herokuapp.com/dynamic_loading/2'
# url = 'https://www.facebook.com/'


# driver_path = '/home/tareq/Desktop/webscraping/selenium/MahmudAhsan/chromedriver_linux64/chromedriver'

# driver = webdriver.Chrome(driver_path)
# driver.get(url)

# driver.find_element_by_xpath('//*[@id="username"]').send_keys('tomsmith')
# driver.find_element_by_xpath('//*[@id="password"]').send_keys('SuperSecretPassword!')
# driver.find_element_by_xpath('//*[@id="login"]/button').click()

# driver.find_element_by_xpath('//*[@id="start"]/button').click()
# driver.implicitly_wait(10)

# txt = driver.find_element_by_xpath('//*[@id="finish"]/h4').text
# print(txt)

# driver.find_element_by_xpath('//*[@id="email"]').send_keys('******')
# driver.find_element_by_xpath('//*[@id="pass"]').send_keys('******')
# # driver.implicitly_wait(5)
# driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()




# driver.quit()

from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from getpass import getpass 

usr=input('Enter Email Id:') 
# pwd=input('Enter Password:') 
pwd = getpass('Enter Password:')        ## not print password when entere

driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://www.facebook.com/') 
print ("Opened facebook") 
sleep(1) 

username_box = driver.find_element_by_id('email') 
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(1) 

password_box = driver.find_element_by_id('pass') 
password_box.send_keys(pwd) 
print ("Password entered") 

login_box = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button') 
login_box.click() 

print ("Done") 
input('Press anything to quit >') 
driver.quit() 
print("Finished")

