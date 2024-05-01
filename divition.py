def div(x,y):
     if y == 0:
        print("Can't divide by 0")
        print("0 replaced by 1")
        y = 1
        
     print(f'{x} / {y} is equal to {x / y}')
     return x / y
