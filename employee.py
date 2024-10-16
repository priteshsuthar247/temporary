class employee:
    name = " "
    dept = " "
    sal = 0
    
    def take_input(e):
        e.name = input("Enter Name: ")
        e.dept = input("Enter Dept: ")
        e.sal = int(input("Enter Salary: "))
        
    def display(e):
        print(f"Name: {e.name}")
        print(f"Dept: {e.dept}")
        print(f"Sal: {e.sal}")
        
e = employee()
e.take_input()
e.display()
