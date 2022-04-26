import requests
from bs4 import BeautifulSoup
from pprint import pprint

HEADERS = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

Site = 'https://www.bundestag.de'
max_offset = 736 + 1
Person = {}

with open('Data/Offset_0.html', 'r', encoding='utf-8') as file:
    Offset = file.read()

soup = BeautifulSoup(Offset, 'lxml')

all_people = soup.find_all(class_='col-xs-4 col-sm-3 col-md-2 bt-slide')
for i in range(len(all_people)):
    people_link = f"{Site}{all_people[i].find('a')['href']}"
    people_name = all_people[i].find('div', class_='bt-teaser-person-text').find('h3').text

    internet = requests.get(people_link, headers=HEADERS).text
    soup2 = BeautifulSoup(internet, 'lxml')
    r = soup2.find(class_='col-xs-12 col-md-4').find_all('li')

    dic_person = {}
    for i in r:
        dic_person[i.text.strip()] = i.find('a')['href']

    Person[people_name] = dic_person
pprint(Person)
