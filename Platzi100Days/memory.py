from random import choices

CARACTERES = ['\"', '#', '$', '%', '(', ')', '/', '&']

seleccion = choices(CARACTERES, k = 4)

simbolos = ''
for char in seleccion:
    simbolos += char

print(simbolos)