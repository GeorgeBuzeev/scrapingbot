import requests
import re
from bs4 import BeautifulSoup

class Tovar:
    def __init__(self, brand, name, price):
        self.brand = brand
        self.name = name
        digits_price = re.sub("\D", "", price)
        self.price = int(digits_price)

    @property   #свойство, а не функция
    def clean_name(self):
        return re.sub(r'[^\x00-\x7f]',r'', self.name).lstrip()

    #@property
#    def delete_spaces(self):
    #    return self.name.replace(" ", "")

    @property
    def tokens(self):
        tokens = self.clean_name.split()
        return tokens

    def print_tovar(self):
        print(self.brand, self.clean_name, '-', self.price)

def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default

def scrappage(link):  #парсим подкаталог
    page = requests.get(link)
    #print(page) #выыодит на экрат simple html
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify()) #выводит красивый html с табуляцией

    divwitha = soup.find('div', class_='breadcrumbs').find('div') #поиск в div класс wr
    nyshnajassilka = divwitha.find_all('a')[-1:][0] #берем ссылку, в которой находится бренд
    brand = nyshnajassilka.get_text().lower() #из любого регистра нижний

    if 'harvia' in brand or "tylo" in brand or 'kastor' in brand:
        name = divwitha.find_all('span')[-1:][0].get_text()
        price = soup.find('div', class_='price').find('span').get_text()
        tovar = Tovar(brand, name, price)
        tovar.print_tovar()
        all_tovar.append(tovar)


def atelie(link):    #парсим заглавную страницу
    print("checking: " + link)
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    blocs = soup.find_all('div', class_='prod_name')
    for bloc in blocs:
        ahrefsoup = bloc.find('a')
        ahref = ahrefsoup["href"]
        scrappage(link = 'https://ateliesaun.ru/' + ahref)

    page = safe_cast(soup.find('a', class_='pager_act').get_text(), int)
    next_page = page + 1
    alllinks = soup.find('div', class_='link_pages').find_all('a')
    next_page_link = None
    for links in alllinks:
        page_number = safe_cast(links.get_text(), int, 0)
        if next_page == page_number:
            next_page_link = links['href']
    if next_page_link:
        newlink = 'https://ateliesaun.ru/' + next_page_link
        print(newlink)
        atelie(link = newlink)

def save_to_csv(tovary):
    # пройти по всем объекта  и сохранить их в csv
    import csv
    with open('atelie.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['brand', 'name', 'price'])
        for tovar in tovary:
            writer.writerow([tovar.brand, tovar.name, tovar.price])

def save_compound(tovary):
    import csv
    with open('atelie.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['brand', 'name', 'price'])
        for tovar in tovary:
            writer.writerow([tovar.brand, tovar.name, tovar.price])

all_tovar = []
links = [
"https://ateliesaun.ru/pechi-dlya-bani/",
"https://ateliesaun.ru/elektrokamenki-dlya-saun/",

]
for link in links:
    atelie(link = link)

print("guess...it's over")

#compunds = [[1,2,3], [4,5,6], [8,6,3]]

#for tovar in all_tovar:
#    equals = []
#    for searchTovar in all_tovar:
#        if tovar == searchTovar:
#            equals.append(searchTovar)
#    compunds.append(equals)
#save_compound(compunds)



save_to_csv(all_tovar)
