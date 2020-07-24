def ordenar_ascendente(lista_numeros, orden):

    for i in range(1, len(lista_numeros)):
        valor_actual = lista_numeros[i]
        posicion_actual = i

        if orden == 'asc':
            while posicion_actual > 0 and lista_numeros[posicion_actual - 1] > valor_actual:
                lista_numeros[posicion_actual] = lista_numeros[posicion_actual - 1]   
                posicion_actual -= 1
        elif orden == 'dsc':
            while posicion_actual > 0 and lista_numeros[posicion_actual - 1] < valor_actual:
                lista_numeros[posicion_actual] = lista_numeros[posicion_actual - 1]   
                posicion_actual -= 1

        lista_numeros[posicion_actual] = valor_actual
    
    return lista_numeros
        
def obtener_numeros():
    print('Inserta los números a ordenar. Inserta X para terminar de insertar.\n')
    lista = []
    num = 0

    while num != 'x':
        num = input('Número: ')
        num = num.lower()
        if num != 'x':
            num = float(num)
            lista.append(num)  


    print(f'\n Lista de números: {lista}')
    return lista      


if __name__ == "__main__":
    print('''ORDENA TUS NUMEROS''')
    lista = obtener_numeros()
    orden = input('\n¿Cómo quieres ordenar los números? asc/dsc: ')
    orden = orden.lower()
    lista_ordenada = ordenar_ascendente(lista, orden)
    print(f'\nLista ordenada: {lista_ordenada}')
