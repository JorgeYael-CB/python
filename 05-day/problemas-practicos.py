

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



print( devolver_distintos(10, 20, 30) ) # 30
print( devolver_distintos(1, 2, 3) ) # 1
print( devolver_distintos(5, 5, 1) ) # 3