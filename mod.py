
def modul(x,y):
     if y == 0:
        print("Can't divide by 0")
        print("0 replace by 1")
        y = 1

     print(f"{x} modul of {y} is {x % y}")
     return x % y
