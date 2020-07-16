from random import choice

MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']


def generador_contrasena(longitud, caracteres):

    password = ''
    for _ in range(longitud):
        caracter = choice(caracteres)
        password = password + caracter

    return password


def elegir_caracters():
    elegidos = []
    eleccion = input('\n¿Deseas incluir mayúsculas? Si/No: ').lower()
    if eleccion == 'si':
        elegidos.append('MAYUS')
    
    eleccion = input('\n¿Deseas incluir minúsculas? Si/No: ').lower()
    if eleccion == 'si':
        elegidos.append('MINUS')

    eleccion = input('\n¿Deseas incluir números? Si/No: ').lower()
    if eleccion == 'si':
        elegidos.append('NUMS')

    eleccion = input('\n¿Deseas incluir caracteres especiales? Si/No: ').lower()
    if eleccion == 'si':
        elegidos.append('CHARS')

    return elegidos


def generar_lista_caracteres(tipos_caracteres):

    lista_caracteres = []
    
    for tipo in tipos_caracteres:
        if tipo == 'MAYUS':
            lista_caracteres.extend(MAYUS)
        if tipo == 'MINUS':
            lista_caracteres.extend(MINUS)
        if tipo == 'NUMS':
            lista_caracteres.extend(NUMS)
        if tipo == 'CHARS':
            lista_caracteres.extend(CHARS)

    return lista_caracteres


if __name__ == "__main__":
    numero_caracteres = int(input('\nDefine la longitud de tu contraseña: '))
    caracteres_elegidos = elegir_caracters()
    lista_caracteres_elegidos = generar_lista_caracteres(caracteres_elegidos)
    contraseña_generada = generador_contrasena(numero_caracteres, lista_caracteres_elegidos)

    print(f'\n\tContraseña generada: {contraseña_generada}')
