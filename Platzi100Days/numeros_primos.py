def calcular_primos(numero_max):
    """
    Calcula una serie de números primos hasta el número máximo indicado.

    Parámetros:
    numero max int > 0

    Retorna:
    Lista con serie de numeros primos
    """
    numeros = [num for num in range(numero_max + 1)]
    primos = []

    for num in numeros:
        primo = is_primo(num)
        if primo:
            primos.append(num)                
    
    return primos


def is_primo(numero):
    """Recibe un número entero y determina si es primo

    Parámetros:
    numero int > 0

    retorna:
    True or False"""

    if numero < 2:
        return False
    elif numero == 2:
        return True
    elif numero > 2 and numero % 2 == 0:
        return False
    else: 
        for i in range(3, numero):
            if numero % i == 0:
                return False
    return True


def main():
    print('\nEscribe un número para listar todos los números primos hasta ese número.')
    limite = int(input('\nIngresa el número máximo: '))
    numeros_primos = calcular_primos(limite)
    print(f'\nNúmeros primos del 1 hasta el {limite}:')
    for numero in numeros_primos:
        print(numero)


if __name__ == "__main__":
    main()