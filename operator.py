class demo:
    x=0
    def __add__(a,b):
        return b.x + a.x

d1 = demo()
d2 = demo()
d1.x = 10
d2.x = 20
print(d1+d2)
