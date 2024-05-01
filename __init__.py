from addition import add
from multiplication import mul
from divition import div

def game():
     score = 0

     while True:
         print('======== Menu ========'
         '\n3. Divition'
         '\n2. Multiplication'
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
             result = mul(num_1, num_2)
         elif option == 3:
             result = div(num_1, num_2)
         elif option == 4:
             pass
         elif option == 5:
             pass
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
