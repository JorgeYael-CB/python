
def suma( num1, num2, *args, **kwargs ):
  print( f'Primer valor: {num1}' );
  print( f'Segundo valor: {num2}' );
  print( args );
  print( kwargs );
  total = 0

  for arg in args:
    print(f'arg = {arg}')

  for k, value in kwargs.items():
    print(f'{k} = {value}')
    total += value

  return total


print( suma(15, 50, 100, 200, 300, 400, 500, a = 10, b = 20, c = 30) )