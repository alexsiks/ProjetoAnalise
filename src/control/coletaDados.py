# Python3 code implementing web scraping using lxml

import requests

# import only html class
from lxml import html

# url to scrap data from
url = 'https://www.geeksforgeeks.org'

# path to particular element
path = '//*[@id ="post-183376"]/div / p'

# get response object
response = requests.get(url)

# get byte string
byte_data = response.content

# get filtered source code
source_code = html.fromstring(byte_data)

# jump to preferred html element
tree = source_code.xpath(path)

# print texts in first element in list
print(tree[0].text_content())
