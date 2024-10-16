class mother:
    eyes = "brown"
    
class father:
    height = 6
    build = "muscular"
    
class son(mother,father):
    def display(s):
        print(f"{s.eyes}, {s.height} ft, {s.build}")
        
s1 = son()
s1.display()
