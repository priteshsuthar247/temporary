def display(a,b):
    print(f"A: {a} \nB: {b}\n")
    
def swapping_without_temp():
    a = 10
    b = 20
    a,b = b,a
    display(a,b)
    
def swapping_using_temp():
    a = 10
    b = 20
    temp = a
    a = b
    b = temp
    display(a,b)
    
print("Swapped without temp")
swapping_without_temp()

print("Swpped using temp")
swapping_using_temp()
