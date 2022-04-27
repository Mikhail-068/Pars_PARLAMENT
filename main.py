import json
import numpy as np
from time import sleep
import requests
from bs4 import BeautifulSoup
from pprint import pprint

HEADERS = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

Site = 'https://www.bundestag.de'
max_offset = 736 + 1


# n = 0
# url_all = f'https://www.bundestag.de/ajax/filterlist/de/abgeordnete/862712-862712?limit=20&noFilterSet=true&offset={n}'
# html_ = requests.get(url_all, headers=HEADERS).text

def save_img(link, name):
    img_save = requests.get(link).content
    with open(f'Data/Images_720/{name}.jpg', 'wb') as f:
        f.write(img_save)


with open('Data/link_offset.txt', 'r', encoding='utf-8') as f:
    links = f.read()
list_links = links.split('\n')[:-1]

Person = {}
list_pers = []
c = 1

for link in range(720, max_offset):
    r = requests.get(list_links[link], headers=HEADERS).text
    soup = BeautifulSoup(r, 'lxml')

    all_people = soup.find_all(class_='col-xs-4 col-sm-3 col-md-2 bt-slide')

    for pers in all_people:
        try:
            person = f"{Site}{pers.find('a')['href']}"
            Response = requests.get(person, headers=HEADERS).text
            soup2 = BeautifulSoup(Response, 'lxml')
            img = f"{Site}{soup2.find(class_='bt-bild-standard pull-left').find('img')['data-img-md-normal']}"
            name = soup2.find(class_='bt-bild-standard pull-left').find('img')['title']
            save_img(img, name)
            print(name, 'готово!')
        except:
            print(f"С {name} не получилось...")
            continue
    print(link, 'страница готова!\n\n')
