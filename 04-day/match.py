cliente = {'nombre': 'Yael', 'edad': 20, 'ocupacion': 'FullStack Developer'}
pelicula = {
  'titulo': 'Matrix',
  'ficha_tecnica': {
    'protagonista': 'Keanu reeves',
    'director': 'Lana y Lilly Wachowski'
  }
}

elementos = [cliente, pelicula, 'Libro']

for element in elementos:
  match element:
    case {'nombre': nombre, 'edad': edad, 'ocupacion': ocupacion}:
      print(f'Es un cliente: {nombre, edad, ocupacion}')
    case {'titulo': titulo, 'ficha_tecnica': {'protagonista': protagonista, 'director': director}}:
      print(f'es una pelicula: {titulo, protagonista, director}')
    case _:
      print('No se que es esto');




# serie = 'N-02'

# Sentencia IF
# if serie == 'N-01':
#   print('Samsung')
# elif serie == 'N-02':
#   print('Nokia')


# match
# match serie:
#   case 'N-01':
#     print('Samsung')
#   case 'N-02':
#     print('Nokia')
#   case _:
#     print('Desconozco del tema')