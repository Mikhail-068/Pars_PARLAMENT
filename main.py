import json

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



with open('Data/link_offset.txt', 'r', encoding='utf-8') as f:
    links = f.read()
list_links = links.split('\n')[:-1]



Person = {}
list_pers = []
c = 1



for link in range(0, 730, 20):
    print(link)
    r = requests.get(list_links[link], headers=HEADERS).text
    soup = BeautifulSoup(r, 'lxml')

    all_people = soup.find_all(class_='col-xs-4 col-sm-3 col-md-2 bt-slide')


    for i,pers in enumerate(all_people):
        people_link = f"{Site}{pers.find('a')['href']}"
        people_name = pers.find('div', class_='bt-teaser-person-text').find('h3').text


        internet = requests.get(people_link, headers=HEADERS).text
        soup2 = BeautifulSoup(internet, 'lxml')
        r = soup2.find(class_='col-xs-12 col-md-4').find_all('li')

        dic_person = {}

        for i in r:
            dic_person[i.text.strip()] = i.find('a')['href']
        Person[people_name] = dic_person


with open('Person2.json', 'w', encoding='utf-8') as f:
    json.dump(Person, f, indent=4, ensure_ascii=False)



