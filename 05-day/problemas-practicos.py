

def devolver_distintos(par1: int, par2: int, par3: int):
  array = [par1, par2, par3]

  num_max = num_min = array[0]
  suma = 0

  for num in array:
    if num > num_max:
      num_max = num
    if num < num_min:
      num_min = num
    suma += num

  if suma > 15:
    return num_max
  elif suma < 10:
    return num_min
  else:
    return suma // len(array)


def ordenar_palabra( palabra: str ):
  lista = list( palabra )
  lista.sort()

  palabras = set( lista )
  print( palabras )


def check_zeros( *args ):
  number = -1;

  for n in args:
    if number == 0 and number == n:
      return True
    else:
      number = n
  return False


def contar_primos( number: int ):
  for n in range(2, number + 1, 1):
    if n > 3 and (n % 2 == 0 or n % 3 == 0):
      print(f'No es primo: {n}')
    else:
      print(f'Si es primo: {n}')


contar_primos(100)



# print( check_zeros(1, 2, 3,4 ,5, 0, 0) ) #true
# print( check_zeros(1, 2, 3,4 ,5, 0, 1) ) #false


# ordenar_palabra('Hello World')

# print( devolver_distintos(10, 20, 30) ) # 30
# print( devolver_distintos(1, 2, 3) ) # 1
# print( devolver_distintos(5, 5, 1) ) # 3

