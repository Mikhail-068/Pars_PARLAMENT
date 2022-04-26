import requests
from bs4 import BeautifulSoup

HEADERS = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

# html = 'https://www.bundestag.de/abgeordnete'
max_offset = 736 + 1

# n = 0
# url_all = f'https://www.bundestag.de/ajax/filterlist/de/abgeordnete/862712-862712?limit=20&noFilterSet=true&offset={n}'
# html_ = requests.get(url_all, headers=HEADERS).text



with open('Data/Offset_0.html', 'r', encoding='utf-8') as file:
    Offset = file.read()

soup = BeautifulSoup(Offset, 'lxml')
r = soup.find(class_='col-xs-4 col-sm-3 col-md-2 bt-slide').find(class_='bt-teaser-person-text').find('h3').text
print(r)
