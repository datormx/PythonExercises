import random

def busqueda_binaria(objetivo, lista_numeros, bajo, alto):
    if bajo > alto:
        return False

    medio = (alto + bajo) // 2
    print(f'{lista_numeros[bajo]}  {lista_numeros[alto-1]}  {lista_numeros[medio]}')

    if lista_numeros[medio] == objetivo:
        return (True, medio)
    elif lista_numeros[medio] > objetivo:
        return busqueda_binaria(objetivo, lista_numeros, bajo, medio - 1)
    elif lista_numeros[medio] < objetivo:
        return busqueda_binaria(objetivo, lista_numeros, medio + 1, alto)    


if __name__ == "__main__":
    
    objetivo = int(input('Escoge un entero a buscar: '))
    lista_numeros = []

    for _ in range(101):
        lista_numeros.append(random.randint(1,101))

    lista_numeros = set(lista_numeros)
    lista_numeros = list(lista_numeros)
    lista_numeros.sort()

    print(lista_numeros)

    bajo = 0
    alto = len(lista_numeros)

    encontrado, posicion = busqueda_binaria(objetivo, lista_numeros, bajo, alto)
    
    if encontrado:
        print(f'El numero {objetivo} se encontró en la posición {posicion}')
    else:
        print(f'El numero {objetivo} no se encontró')



