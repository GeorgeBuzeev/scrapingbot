class Tovar:
    def __init__(self, brand, name, price):
        self.brand = brand
        self.name = name
        digits_price = re.sub("\D", "", price)
        self.price = int(digits_price)


    def print_tovar(self):
        print(self.brand, self.name, '-', self.price)
