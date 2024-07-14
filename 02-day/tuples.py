
# mi_tuple = 1, 2, 3
# mi_tuple = (1, 2, 3)
mi_tuple = (5, 10.5, 'Hello', ['A', 'B', 'C'])
mi_tuple = list( mi_tuple )
mi_tuple = tuple( mi_tuple )


mi_tuple_2 = (1, 2, 3)
a, b, c = mi_tuple_2 #tambien sirve en los arreglos y diccionarios



# print( mi_tuple.index(5) )
print( mi_tuple )
print( a, b, c )

print( mi_tuple_2.count(1) ) # cuantas veces aparece el valor