import requests
from bs4 import BeautifulSoup

server_response = requests.get('https://www.bbc.com/')
server_response_code = server_response.status_code
print('Server Response Code: ',server_response_code)

html_data = server_response.content
formatted_html = BeautifulSoup(html_data, 'html.parser')

print(formatted_html.title)                 # <title>BBC - Homepage</title>
print(formatted_html.title.string)          # BBC - Homepage
print(formatted_html.title.text)            # BBC - Homepage




# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html_code = urlopen('https://www.bbc.com/')

# # print(html_code.read())       # raw html data
# bs_obj = BeautifulSoup(html_code.read(),'html.parser')

# # print(bs_obj)       # formatted html data

# # title = bs_obj.title            # return title tag with element
# title = bs_obj.title     # return only title text
# print(title)


# import requests
# from bs4 import BeautifulSoup

# # s_res = requests.get('https://www.aljazeera.com')

# # print(s_res.status_code)

# # html_code = s_res.content
# html_doc = """<html><head><title>The Dormouse's story</title></head>
# <body>

# <div class='blue' > this is my p tag <a href="url">a link</a>
#     <a href="url"> 2nd link</a>
#     <a href="url">3rd  link</a>
#  </div>
# <p class="title"><b>The Dormouse's story</b></p>

# <div> hello div </div>

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister brother " id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>
# """
# soup = BeautifulSoup(html_doc,'html.parser')

# # print(soup.prettify())
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.title.parent)

# # print(soup.p)
# # print(soup.p.parent.text)
# # print(soup.p.find_all('a'))

# # all_anchor = soup.p.find_all('a')
# # print(all_anchor)
# # print(soup.find(id='link3').get('href'))

# # print(soup.find(id='link3')['class'])
# # all_anchor = soup.find_all('a')
# # print(all_anchor)
# # for link in all_anchor:
#     # print(link.get('href'))
#     # print(link.get('class'))

# # print(soup.get_text())





# # all_headings = soup.find_all([])
