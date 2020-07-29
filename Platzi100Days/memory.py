import random

CARACTERES = ['\"', '#', '$', '%', '(', ')', '/', '&']

seleccion = random.choices(CARACTERES, k = 4)

simbolos = {}
for i, char in enumerate(seleccion):
    simbolos[i] = char

simbolos_desordenados = list(simbolos.values())
random.shuffle(simbolos_desordenados)
simbolos_desordenados = ''.join(simbolos_desordenados)

# print(simbolos) #Scaffolding

print(f'Los símbolos fueron: {simbolos_desordenados}. Adivina el orden en que se ingresaron.')

simbolos_elegidos = {}
while simbolos_elegidos != simbolos:    

    simbolos_ingresados = input('\nIngresa todos los simbolos en el orden: ')
    
    for i, char in enumerate(simbolos_ingresados):
        simbolos_elegidos[i] = char
    
    if simbolos_elegidos != simbolos:
        print('\tIncorrecto. Intenta de nuevo.')

print(f'¡Felicidades! El orden es {simbolos}.')



