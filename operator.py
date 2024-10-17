class demo:
    x=0
    def __add__(a,b):
        return a.x + b.x

a = demo()
a.x = 10
print(a+a)
