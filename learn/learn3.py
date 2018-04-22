# data = ["john", "daniel", "something", "it", "bobby", "jake"]
#
# for dat in data:
#     print(dat)

class Person:
    def __init__(self, name, nik, date):
        self.name = name
        self.nik = nik
        self.date = date

    def getgod(self):
        god = 2018 - self.date
        return god

def nnd(name, nik, date):
    return name+' '+' '+nik+' '+' '+date

data2 = [["john", "sis", 1990], ["bobby", "sas", 1987], ["taurel", "nani", 1995]]

# for dat in data2:
#     nnd(dat[0], dat[1], str(dat[2]))

huycy = []
# for dat in data2:
#     huycy.append(nnd(dat[0], dat[1], str(dat[2])))
# print(huycy)

for dat in data2:
    person = Person(dat[0], dat[1], dat[2])
    huycy.append(person)

for person in huycy:
    print(person.getgod())
