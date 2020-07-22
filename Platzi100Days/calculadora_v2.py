import math

def calculadora(numeros, operacion):
    if operacion == '1':
        resultado = sum(numeros)
    elif operacion == '2':
        resultado = 1
        for numero in numeros:
            resultado = resultado * numero
    
    print(resultado)
    return resultado


def generador_lista_numeros(cantidad):
    list_numeros = []
    for i in range(cantidad):
        numero = float(input(f'Ingresa el número {i+1}: '))
        list_numeros.append(numero)    
    
    return list_numeros


def run():
    print("""Calculadora V2.0
    Ingresa una cantidad de números y la operación que harás.""")
    operacion = input("""
    1) Suma
    2) Multiplicación

    Escoge la operación: """)

    cantidad_numeros = int(input('\nIngresa con cuántos números harás el cálculo: '))
    numeros = generador_lista_numeros(cantidad_numeros)

    resultado = calculadora(numeros, operacion)
    print(f'\n\nRESULTADO = {resultado}')


if __name__ == "__main__":
    run()