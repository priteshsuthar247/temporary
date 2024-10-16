class vehicle:
    def use(v):
        print("Created in factory")
    def display(v):
       print("display number of wheels")

class bike(vehicle):
    def display(b):
        print("2 wheels")

v = vehicle()
v.use()
v.display()
b = bike()
b.use()
b.display()
