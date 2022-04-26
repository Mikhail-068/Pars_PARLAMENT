import requests
from bs4 import BeautifulSoup

HEADERS = {'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

html = 'https://www.bundestag.de/abgeordnete'

n=200
url_all =  f'https://www.bundestag.de/ajax/filterlist/de/abgeordnete/862712-862712?limit=20&noFilterSet=true&offset={n}'
r = requests.get(url_all, headers=HEADERS)
print(r)