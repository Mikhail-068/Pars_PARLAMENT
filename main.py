import requests
from bs4 import BeautifulSoup

HEADERS = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

# html = 'https://www.bundestag.de/abgeordnete'
max_offset = 736 + 1

n = 0
url_all = f'https://www.bundestag.de/ajax/filterlist/de/abgeordnete/862712-862712?limit=20&noFilterSet=true&offset={n}'
html_ = requests.get(url_all, headers=HEADERS).text



with open('Data/Offset_0.html', 'w', encoding='utf-8') as file:
    file.write(html_)
