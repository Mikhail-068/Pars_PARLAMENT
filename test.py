import json

import requests
from bs4 import BeautifulSoup
from pprint import pprint

HEADERS = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
max_offset = 736 + 1


n = 0
for n in range(max_offset):
    url = f'https://www.bundestag.de/ajax/filterlist/de/abgeordnete/862712-862712?limit=20&noFilterSet=true&offset={n}'
    with open('Data/link_offset.txt', 'a', encoding='utf-8') as f:
        f.write(f'{url}\n')
