# Escribe un programa que pida al usuario 2 números, mostrando como salida cuál es el número mayor 
# y la diferencia de uno respecto al otro. En caso de que los números sean iguales, mostrarlo también en pantalla.

if __name__ == "__main__":
    print('**I will tell you which number is bigger**')
    num1 = int(input('Give a number: '))
    num2 = int(input('Give a number: '))

    if num1 > num2:
        print(f'{num1} is bigger than {num2}')
        print(f'The difference {num1} - {num2} = {num1-num2}')
    elif num2 > num1:
        print(f'{num2} is bigger than {num1}')
        print(f'The difference {num2} - {num1} = {num2-num1}')
    elif num1 == num2:
        print(f'{num1} and {num2} are equal.')