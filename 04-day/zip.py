nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 29, 42] # toma el largo de la lista mas corta
ciudades = ['Lima', 'Madrid', 'Ciudad De Mexico']

combinados = list(zip( nombres, edades, ciudades ))


for name, edad, city in combinados:
  print(f'La persona "{name}" tiene "{edad}" years de edad y vive en "{city}" ')