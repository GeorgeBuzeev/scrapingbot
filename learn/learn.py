def nnd(name, nik, date):
    return name+' '+' '+nik+' '+' '+date

def guy1():
    name = 'john'
    nik = 'sis'
    date = '1990'
    return name+' '+' '+nik+' '+' '+date

def guy2():
    name = 'bill'
    nik = 'sas'
    date = '1993'
    return name+' '+' '+nik+' '+' '+date

def guy3():
    name = 'kate'
    nik = 'sos'
    date = '1987'
    return name+' '+' '+nik+' '+' '+date

# не правильно
# mass =[
# guy1, guy2, guy3
# ]

# слишком долго
# odin = guy1()
# dva = guy2()
# tri = guy3()
#
# mass = [
# odin, dva, tri
# ]

mass = [nnd('john', 'sis', '1990'), nnd('bill', 'sas', '1993'), nnd('kate', 'sos', '1987')]

print(mass)

# 'name - john'
#  'nik - sis'
#  'date - 1990'
