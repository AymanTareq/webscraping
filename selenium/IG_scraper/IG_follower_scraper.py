#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


from helium import *


# In[3]:


start_chrome()


# In[4]:


go_to('instagram.com')


# In[6]:


write('arif9h22',into=S('//input[@name="username"]'))


# In[7]:


write('abdullah',into=S('//input[@name="password"]'))


# In[8]:


click("log in")


# In[9]:


click("Not Now")


# In[11]:


click("Not Now")


# In[12]:


go_to('https://www.instagram.com/mehazabien/')


# In[21]:


click('followers')


# In[22]:


followers = find_all(S('//*[@class="FPmhX notranslate  _0imsa "]'))


# In[23]:


import time
time.sleep(3)
scroll_down(num_pixels=1000)


# In[ ]:




