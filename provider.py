class Tovar:
    def __init__(self, brand, name, price):
        self.brand = brand
        self.name = name
        digits_price = re.sub("\D", "", price)
        self.price = int(digits_price)


    def print_tovar(self):
        print(self.brand, self.name, '-', self.price)

class Provider:
    def __init__(self):
        pass

    def get_products(self):
        return []

class NFProvider(Provider):
    def __init__(self, links):
        self.all_tovar = []
        self.links = links

    def get_products(self):
        self.all_tovar = []
        for link in self.links:
            scrap95c(link)
        return self.all_tovar

    def scrappage(self, link):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')

        brand = soup.find('div', class_='det_i').find_all('p')[1].find('a').get_text().lower()

        if brand=='harvia' or brand == 'tylo':
            blocs = soup.find_all('a', class_='dc_item') #передвигаем вправо, чтобы работал if

            for bloc in blocs:
                name = bloc.find_all('p', class_='name')[0].get_text()
                price = bloc.find('p', class_='price').get_text()
                tovar = Tovar(brand, name, price)
                tovar.print_tovar()
                self.all_tovar.append(tovar)


    def scrap95c(self, link):
        print("ya obrabativayu: " + link)
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        blocs = soup.find_all('div', class_='cat_item')
        for bloc in blocs:
            ahrefsoup = bloc.find('a', class_='name')
            ahref = ahrefsoup["href"]
            self.scrappage(link = 'https://www.95c.ru' + ahref)

        ifnextpage = soup.find('a', class_='next_page')
        if ifnextpage:
            newlink = 'https://www.95c.ru' + ifnextpage["href"]
            print(newlink)
            self.scrap95c(link = newlink)
