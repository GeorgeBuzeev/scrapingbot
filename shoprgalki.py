
foo = "a"
bar = "b"
soos = foo + bar
print(soos) # "ab"
print(foo + bar) # "ab"
print(foo, bar) # "ab"
print("a" + "b") # "ab"
print("a", "b") # "ab"


foo = "a"
bar = 5
bar2 = "5"
some = foo + bar

def koza():
    a = 5 + 6

def bok(a):
    b = a + 5

def koza2():
    a = 5 + 6
    return 5 + 6

def bok2(a):

    return a + 5

z = koza() # ...
print(z) # ...

x = bok(1) # ...
print(x) # ...

y = koza2() # ...
print(y) # 11
###############
class A:
    __init__(self, sobaka):
        self.sobaka = sobaka

    def minused(a):
        return self.sobaka - a

    def minuse(a):
        self.sobaka = self.sobaka - a

a = A(10)
z = a.sobaka
print(z) # 10
b = a.minused(3)
c = a.sobaka
print(b) # 7
print(c) # 10

i = a.minuse(3)
j = a.sobaka
print(i) # ...
print(j)
