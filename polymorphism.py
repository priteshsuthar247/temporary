class vehicle:
    def display(v):
       print("display number of wheels")

class bike(vehicle):
    def display(b):
        print("2 wheels")

v = vehicle()
v.display()
b = bike()
b.display()
