from addition import add
from subtraction import res 
from multiplication import mul
from divition import div
from pow import potencia

def game():
     score = 0

     while True:
         print('======== Menu ========'
         '\n5. Power'
         '\n4. Divition'
         '\n3. Multiplication'
         '\n2. Subtraction'
         '\n1. Add'
         '\n0. Exit')

         option = int(input('\nChoice an option: '))

         if option == 0:
             print(f"Your total score was {score}")
             break

         num_1 = int(input('Enter first number: '))

         num_2 = int(input('Enter second number: '))

         answer = int(input('Enter you answer: '))

         if option == 1:
             result = add(num_1, num_2)
         elif option == 2:
             result = res(num_1, num_2) 
         elif option == 3:
             result = mul(num_1, num_2)
         elif option == 4:
             result = div(num_1, num_2)
         elif option == 5:
             result = potencia(num_1, num_2)
         elif option == 6:
             pass

         if result == answer:
             score += 1
             print('Correct!!')

         else:
             print('Incorrect')
             print(f'======== Game Over ========'
             f'\nYou score is {score}')

game()
