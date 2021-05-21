import requests
import lxml.html as lh
import pandas as pd

## This exercise available in :
# ## https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059

url = "https://pokemondb.net/pokedex/all"
page = requests.get(url)
html_doc = lh.fromstring(page.content)
# print(html_doc)
tr_elements = html_doc.xpath('//tr')

# print(len(tr_elements))
# print(type(tr_elements))
# sanity_check = [len(T) for T in tr_elements[:12]]
# print(sanity_check)
# now create a empty list
col = []
i = 0

# for each row , store each first element i,e, header and
# an empty list
for t in tr_elements[0]:
    i += 1
    name = t.text_content()
    # print(f"{i}:{name}")
    col.append((name,[]))

# print(len(col))
# print(col)
# since our first row is the header , data is stored on the
# second row onwards
for j in range(1,len(tr_elements)):
    # T is our j'th row
    T = tr_elements[j]

    # if row is not of size 10, the //tr data is not from our table
    if len(T) != 10:
        break
    # i is the index of our column
    i = 0
    # Iterate through each element of the row
    for t in T.iterchildren():
        data = t.text_content()
        # check if row is empty
        if i > 0:
            # convert any numerical value to integers
            try:
                data=int(data)
            except:
                pass
        # append the data to the empty list of the i'th column
        col[i][1].append(data)
        # Increment i for the next column
        i += 1

# print([len(C) for (title,C) in col])

# now it's time to create DataFrame
dict = {title:column for (title,column) in col}
df = pd.DataFrame(dict)
#now export as csv
df.to_csv('pokedex.csv', index=False, encoding='utf-8')
# print(df.head())
# print(len(dict))
# print(type(df))
# print(dict)

print("Okay")