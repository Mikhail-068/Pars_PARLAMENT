import json

import requests
from bs4 import BeautifulSoup
from pprint import pprint

HEADERS = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

with open('Person2.json') as f:
    man = json.load(f)


new = {}
# for i in range(len(links)):
#     for n in range(len(links[i])):
#         new[links[i][n].keys()] = links[i][n].v
# for i in range(20):
#     key_ = list(links[i].keys())
#     val_ = list(links[i].values())
#     for n in range(len(key_)):
#         new[key_[n]] = val_[n]

pprint(man)
