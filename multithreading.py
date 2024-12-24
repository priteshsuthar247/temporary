import threading
def print_cube(n):
    print("Cube:",n * n * n)

def print_square(n):
    print("Square:",n*n)


t1 = threading.Thread(print_square(10))
t2 = threading.Thread(print_cube(10))

t1.start()
t2.start()

t1.join()
t2.join()
