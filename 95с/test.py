class Animal:
    def __init__(self, name):
        self.name = name
        self.age = 35

    def say_your_name(self):
        print("my name is " + self.name)

    def say_your_name_to(self, another):
        print("hello, " + another + ", my name is "+ self.name)

    def say(self, huy, pizda):
        print(self)
        print(huy)
        print(pizda)

    def make_sound(self):
        print("I cant! I dont know Who i am")

class Dog(Animal):
    def make_sound(self):
        print("WOOF!")

# poppy = Animal("poppy")
# poppy.say_your_name()
# poppy.say_your_name_to("alexey")
# poppy.make_sound()
#
# doggy = Dog("sobaka1")
# doggy.say_your_name()
# doggy.make_sound()

class Tovar:
    def __init__(self, brand, price, model):
        self.brand = brand
        self.price = price
        self.model = model

    def print_full_name(self):
        print(self.brand, self.model, " - ", self.price)

tovar1 = Tovar("kotlovan", 13000, "AV145")
tovar2 = Tovar("kotlovan", 14000, "AV135")
tovar3 = Tovar("kotlovan", 120, "AV15")
tovar4 = Tovar("balagan", 120, "AV15")

tovary = [tovar1, tovar2, tovar3]
tovary.append(tovar4)

for tovar in tovary:
    if tovar.brand == "balagan":
        tovar.print_full_name()
