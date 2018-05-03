massiv = []

##### SITE ONE 95C

import requests
import re
from bs4 import BeautifulSoup

class Tovar:
    def __init__(self, brand, name, price, site):
        self.brand = brand
        self.name = name
        digits_price = re.sub("\D", "", price)
        self.price = int(digits_price)
        self.site = site

    @property
    def full_name(self):
        return "".join(self.clean_name.split(" ")).lstrip().rstrip().lower()

    @property
    def clean_name(self):
        return re.sub(r'[^\x00-\x7f]',r'', self.name).lstrip()

    def print_tovar(self):
        print(self.brand, self.clean_name, '-', self.price)

def scrappage(link):
    page = requests.get(link)
        #print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
        #print(soup.prettify())

    brand = soup.find('div', class_='det_i').find_all('p')[1].find('a').get_text().lower()

    if brand=='harvia' or brand == 'tylo':
        blocs = soup.find_all('a', class_='dc_item') #передвигаем вправо, чтобы работал if
            #print(blocs)
        name1 = soup.find('h1', {"id": 'product_name_top'}).get_text()
        for bloc in blocs:
            name = name1 + bloc.find_all('p', class_='name')[0].get_text()
            price = bloc.find('p', class_='price').get_text()
            tovar = Tovar(brand, name, price, '95c')
            tovar.print_tovar()
            massiv.append(tovar)


def scrap95c(link):
    print("checking: " + link)
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    blocs = soup.find_all('div', class_='cat_item')
    for bloc in blocs:
        ahrefsoup = bloc.find('a', class_='name')
        ahref = ahrefsoup["href"]
        scrappage(link = 'https://www.95c.ru' + ahref)

    ifnextpage = soup.find('a', class_='next_page')
    if ifnextpage:
        newlink = 'https://www.95c.ru' + ifnextpage["href"]
        print(newlink)
        scrap95c(link = newlink)

links = [
"https://www.95c.ru/catalog/dlya_sauny/elektrokamenki/",
'https://www.95c.ru/catalog/dlya_sauny/drovyanye_pechi/'
]
for link in links:
    scrap95c(link = link)

print("ya zakonchil")

print('==============NEXT==================')


##### SITE TWO ATELIE


def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default

def scrappage1(link):  #парсим подкаталог
    page = requests.get(link)
    #print(page) #выыодит на экрат simple html
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify()) #выводит красивый html с табуляцией

    divwitha = soup.find('div', class_='breadcrumbs').find('div') #поиск в div класс wr
    nyshnajassilka = divwitha.find_all('a')[-1:][0] #берем ссылку, в которой находится бренд
    brand = nyshnajassilka.get_text().lower() #из любого регистра нижний

    if 'harvia' in brand or 'tylo' in brand or 'helo' in brand: #or 'kastor' in brand:
        name = divwitha.find_all('span')[-1:][0].get_text()
        price = soup.find('div', class_='price_col').find('div', class_='price').find('span').get_text()
        tovar = Tovar(brand, name, price, 'ateliesaun')
        tovar.print_tovar()
        massiv.append(tovar)


def atelie(link):    #парсим заглавную страницу
    print("checking: " + link)
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    blocs = soup.find_all('div', class_='prod_name')
    for bloc in blocs:
        ahrefsoup = bloc.find('a')
        ahref = ahrefsoup["href"]
        scrappage1(link = 'https://ateliesaun.ru/' + ahref)


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

links = [
"https://ateliesaun.ru/pechi-dlya-bani/",
"https://ateliesaun.ru/elektrokamenki-dlya-saun/"
]
for link in links:
    atelie(link = link)

print("guess...it's over")



##### COMPARE ##################
all_massiv = []

#istochniki = ["only", "95c", "ateliesaun", "saunnex"]
istochniki = ["95c", "ateliesaun"]
# dicto = {
#     "95c": Tovar()??,
#     "ateliesaun": Tovar()??
# }
#
# dicto["ateliesaun"] # !!

for mass in massiv:
    alli = {}
    for mas in massiv:
        if mass.full_name == mas.full_name:
            alli[mass.site] = mass
    all_massiv.append(alli)

def save_compound(tovary):
    import csv
    with open('all.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        rows = ['brand', 'name']
        for ist in istochniki:
            rows.append('price' + ist)
        writer.writerow(rows)
        for qqq in all_massiv:
            #row = [qqq["only"].brand, qqq["only"].name] # можно удалить
            main_istochnik = ""
            for ist in istochniki:
                main_tovar = qqq.get(ist, None)
                if main_tovar:
                    main_istochnik = ist
                    break
            row = [qqq[main_istochnik].brand, qqq[main_istochnik].name]
            for ist in istochniki:
                tovar = qqq.get(ist, None)
                if tovar:
                    row.append(tovar.price)
                else:
                    row.append(0)

            writer.writerow(row)
            # for qqq1 in qqq:
            #     writer.writerow([qqq1.brand, qqq1.name, qqq1.price])

        # for tovar in tovary:
        #     writer.writerow([tovar.brand, tovar.name, tovar.price])

save_compound(all_massiv)
