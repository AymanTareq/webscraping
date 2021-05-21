




# import urllib.request
# from bs4 import BeautifulSoup

# # specify the url
# quote_page = "https://www.dailynayadiganta.com/"
# # query the website and return the html to the variable ‘page’
# page = urllib.request.urlopen(quote_page)

# # parse the html using beautiful soup and store in variable `soup`
# soup = BeautifulSoup(page,"html.parser")

# # Take out the <div> of name and get its value
# name_box = soup.find("div", attrs={"class":"news-caption-lead"})

# print(name_box)
# # name = name_box.text # strip() is used to remove starting and trailing
# # print(name)

# # get the index price
# # price_box = soup.find('div', attrs={'class':'price'})
# # price = price_box.text
# # print(price)