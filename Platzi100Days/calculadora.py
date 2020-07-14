def calculadora(num_1, num_2, operador):
    """Recibe dos números y un símbolo de operación y aplica la operación
    a esos dos números
    
    Parámetros
    num_1, num_2 str con símbolos de números
    operador str con símbolo de operador

    Retorna
    Valor de operación resuelta
    operation float o int"""

    operation = num_1 + operador + num_2
    try:
        operation = eval(operation)
    except (NameError, SyntaxError)  as e:
        print(f'\n{e}')
        print('No introduciste un valor numérico o de operación. Intenta de nuevo.')
    else:
        return operation


if __name__ == "__main__":
    numero_1 = input('Ingresa un numero: ')
    numero_2 = input('Ingresa un segundo numero: ')
    simbolo = input('Ingresa el símbolo de la operación: ')
    
    resultado = calculadora(numero_1, numero_2, simbolo)
    if resultado:
        print(f'\n{numero_1} {simbolo} {numero_2} = {resultado}')