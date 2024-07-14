from random import *


name = input('Cual es tu nombre?: ')
random_number = randint(1, 50)

current_attemp = 0
max_attemps = 8
finish_game = False

print(f'Bienvenido {name}, debes adivinar el numero que piensa la maquina, si lo adivinas gaas 5k dolares!, suerte {name}')

while current_attemp <= max_attemps and not finish_game:
  user_number = int(input('Di el numero para ganar: '))

  if user_number > 250 or user_number < 0:
    print('Ese numero es muy grande, intenta de nuevo!')
  elif user_number < random_number:
    print('Oops!, intenta de nuevo aumentando la cantidad...')
  elif user_number > random_number:
    print('Te has pasado!, elige un numero mas chico')
  else:
    finish_game = True
    print(f'GANASTE!, los intentos totales fueron: {current_attemp}')
    print(f'Numero que seleccionaste: {user_number}, numero para ganar: {random_number}')
  current_attemp += 1

if current_attemp >= 8:
  print('Haz perdido!, intenta de nuevo!')