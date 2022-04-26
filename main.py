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



with open('Data/Offset_0.html', 'r', encoding='utf-8') as file:
    Offset = file.read()

soup = BeautifulSoup(Offset, 'lxml')
all_people = soup.find_all(class_='col-xs-4 col-sm-3 col-md-2 bt-slide')
people_link = f"{Site}{all_people[0].find('a')['href']}"
people_name = all_people[0].find('div', class_='bt-teaser-person-text').find('h3').text
# print(people_name)
# print(f"{Site}{people_link}")

internet = requests.get(people_link, headers=HEADERS).text
soup2 = BeautifulSoup(internet, 'lxml')
r = soup2.find(class_='col-xs-12 col-md-4').find_all('li')


dic_person = {}
for i in r:
    dic_person[i.text.strip()] = i.find('a')['href']

pprint(dic_person)


# for people in all_people:
#     people.
