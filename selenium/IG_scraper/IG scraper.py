#!/usr/bin/env python
# coding: utf-8

# In[5]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
print("Tareq")


# In[10]:


import os
import wget


# In[8]:


get_ipython().system('pip3 install wget')


# In[16]:


driver = webdriver.Chrome('/home/tareq/chromedriver_linux64/chromedriver')
driver.get('https://www.instagram.com/accounts/login/')


# In[ ]:





# In[18]:


username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()
username.send_keys("arif9h22")
password.send_keys("abdullah")


# In[19]:


log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


# In[21]:


not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]"))).click()


# In[22]:


not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]"))).click()


# In[23]:


search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
search_box.clear()

keyword = "#cat"
search_box.send_keys(keyword)


# In[24]:


search_box.send_keys(Keys.ENTER)


# In[27]:


driver.execute_script("window.scrollTo(0,5000);")


# In[28]:


images = driver.find_elements_by_tag_name('img')

images


# In[29]:


images = [image.get_attribute('src') for image in images]


# In[30]:


path = os.getcwd()
path = os.path.join(path, keyword[1:]+"s")

os.mkdir(path)
path


# In[31]:


c = 0
for image in images:
    save_as = os.path.join(path, keyword[1:]+str(c)+'.jpg')
    wget.download(image, save_as)
    c += 1

