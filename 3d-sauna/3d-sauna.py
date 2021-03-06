##########   НЕ ДОДЕЛАНО!!!!!!   ###########
import requests
import re
from bs4 import BeautifulSoup

class Tovar:
    def __init__(self, brand, name, price):
        self.brand = brand
        self.name = name
        digits_price = re.sub("\D", "", price)
        self.price = int(digits_price)

    @property  #свойство, а не функция
    def clean_name(self):
        return re.sub(r'[^\x00-\x7f]',r'', self.name).lstrip()

    def print_tovar(self):
        print(self.brand, self.clean_name, '-', self.price)

def scrappage(link):
    page = requests.get(link)
        #print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
        #print(soup.prettify())

    brand = soup.find('div', {"id": 'features'}).find('ul', class_='list-inline')
    brand = brand.find('li').find('div', class_='value')
    brand = brand.get_text().lower().lstrip().rstrip()
    #print(brand)
    if 'harvia' in brand or 'tylo' in brand or 'helo' in brand or 'kastor' in brand:
        name = soup.find_all('span', {"itemprop": 'name'})[-1:][0].get_text()
        price = soup.find('span', class_='price').get_text()
        tovar = Tovar(brand, name, price)
        tovar.print_tovar()
        all_tovar.append(tovar)

def scrap95c(link):
    print("checking: " + link)
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    blocs = soup.find_all('li', class_='product')
    for bloc in blocs:
        ahrefsoup = bloc.find('a')
        ahref = ahrefsoup["href"]
        #print('SSSSSSSSSSSSSSS__' + ahref)
        scrappage(link = 'https://saunex.ru/' + ahref)
        #print(scrappage)

    ifnextpage = soup.find('ul', class_='list-inline').find_all('li')[-1:][0]
    ifnextpage = ifnextpage.find('a', class_='inline-link')
    if ifnextpage:
        newlink = 'https://saunex.ru/' + ifnextpage["href"]
        print(newlink)
        scrap95c(link = newlink)

def save_to_csv(tovary):
    # пройти по всем объекта  и сохранить их в csv
    import csv
    with open('3dsauna.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['brand', 'name', 'price'])
        for tovar in tovary:
            writer.writerow([tovar.brand, tovar.clean_name, tovar.price])

all_tovar = []
links = [
"https://saunex.ru/pechi_dlya_bani_i_sauny/elektrokamenki/",
'https://saunex.ru/pechi_dlya_bani_i_sauny/drovyanye_pechi_/'
]
for link in links:
    scrap95c(link = link)

print("ya zakonchil")

print(all_tovar)
save_to_csv(all_tovar)
