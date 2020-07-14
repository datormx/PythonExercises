from random import randint

def generar_numero():
    """Gener un número pseudo aleatorio del 1 al 100"""

    random_number = randint(1, 100)
    
    return random_number


def adivinar(numero):
    """Notifica si el usuario ingresa un numero mayor, menor o igual a un número determinado.

    Parámetro:
    numero = int > 0"""
    
    numero_usuario = 101
    intentos = 0

    while numero_usuario != numero:
        intentos += 1
        numero_usuario = int(input('\nInserta el número que crees que es: '))
        
        if numero > numero_usuario:
            print('\nEl número es mayor al que insertaste')
        elif numero < numero_usuario:
            print('\nEl número es menor al que insertaste')
        elif numero == numero_aleatorio:
            print(f'\nFelicidades. El número es {numero}.')


if __name__ == "__main__":

    print("Adivina el número del 1 al 100")
    numero_aleatorio = generar_numero()
    adivinar(numero_aleatorio)