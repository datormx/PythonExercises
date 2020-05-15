# Pide al usuario que indique 2 números: uno que servirá como límite y otro para comparar. 
# Si el segundo número es menor al primero, mostrarás un mensaje diciendo 
# “El número ‘x’ se encuentra en el rango, gracias” y en caso contrario dirá “El número ‘x’ 
# excede el límite permitido”.

if __name__ == "__main__":
    print('**I will tell you if the number is in range**')

    limit = int(input('Insert the limit number: '))
    number = int(input('Insert any number: '))

    if number < limit:
        print(f'\nThe number {number} is within range.')
    else:
        print(f'\nThe number {number} exceeds range.')