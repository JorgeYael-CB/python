texto = input('Ingresa un texto: ')
letras = input('Ingresa 3 letras: ')

letras1 = texto.lower().find( letras.lower()[0] )
letras2 = texto.lower().find( letras.lower()[1] )
letras3 = texto.lower().find( letras.lower()[2] )


print( letras1, letras2, letras3 )
print( f'total de letras: {len(texto)}' )
print( f'Primera letra: {texto[0]}, ultima letra: {texto[ len(texto) - 1 ]}' )
print( f'Orden inverso: {texto[::-1]}' )

find_letter_python = 'python' in texto.lower()

print(f'La palabra Python se encuentra en tu texto? {find_letter_python}')