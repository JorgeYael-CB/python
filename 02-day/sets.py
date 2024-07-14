# mi_set = {1, 2, 3, 4, 5}
mi_set = set( [1, 2, 3, 4, 5, 1, 1, 1, 1, (1, 2, 3)] ) # unicos valores acepta
s1 = {1, 2, 3}
s2 = {4, 5, 6}
s3 = s1.union( s2 )

s3.add(7)
s3.remove(7) # da error si no viene
# s3.discard(6) # no da error
s3.pop() # elimina un elemento aleatorio ya que los set no tienen orden
# s3.clear() # reinicia el set



print( s3 )
print( 2 in mi_set ) #tuples, listas, diccionarios.