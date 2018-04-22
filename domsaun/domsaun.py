import requests
import re
from bs4 import BeautifulSoup

class Tovar:
    def __init__(self, brand, name, price):
        self.brand = brand
        self.name = name
        digits_price = re.sub("\D", "", price)
        self.price = int(digits_price)


    def print_tovar(self):
        print(self.brand, self.name, '-', self.price)


def scrappage(link):
    page = requests.get(link)
        #print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
        #print(soup.prettify())

    brand = soup.find('ol', class_='breadcrumb').find_all('li')[-1:][0].find('a').get_text().lower()
    print(brand)
    if 'harvia' in brand or "tylo" in brand or 'kastor' in brand:
        name = bloc.find_all('li', class_='breadcrumb')[-1:][0].find('h1')[0].get_text()
        price = bloc.find('p', class_='price').get_text()
        tovar = Tovar(brand, name, price)
        tovar.print_tovar()
        all_tovar.append(tovar)


def scrap95c(link):
    print("checking: " + link)
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    blocs = soup.find_all('td', class_='title')
    for bloc in blocs:
        ahrefsoup = bloc.find('a')
        ahref = ahrefsoup["href"]
        #print('SSSSSSSSSSSSSSS__' + ahref)
        scrappage(link = 'https://domsaun.ru/' + ahref)

    # ifnextpage = soup.find('a', class_='next_page')
    # if ifnextpage:
    #     newlink = 'https://www.95c.ru' + ifnextpage["href"]
    #     print(newlink)
    #     scrap95c(link = newlink)

def save_to_csv(tovary):
    # пройти по всем объекта  и сохранить их в csv
    import csv
    with open('95c.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['brand', 'name', 'price'])
        for tovar in tovary:
            writer.writerow([tovar.brand, tovar.name, tovar.price])

all_tovar = []
links =[
'https://domsaun.ru/catalog/electro/harvia/',
'https://domsaun.ru/catalog/electro/helo/',
'https://domsaun.ru/catalog/electro/tylo/',
'https://domsaun.ru/catalog/fire/harvia/',
'https://domsaun.ru/catalog/fire/kastor/'
]
for link in links:
    scrap95c(link = link)

print("ya zakonchil")

print(all_tovar)
save_to_csv(all_tovar)
