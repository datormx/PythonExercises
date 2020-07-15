vocals = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'u', 'ú']

def traductor(palabra):
    palabra = palabra.lower()
    for vocal in vocals:
        if palabra[0] == vocal:
            palabra = palabra + 'way'
            palabra = palabra.capitalize()
            return palabra  
        elif palabra[0] != vocal:
            primera_letra = palabra[0]
            palabra = palabra[1:]
            palabra = palabra + primera_letra + 'ay'
            palabra = palabra.capitalize()
            return palabra                    


if __name__ == "__main__":
    palabra = input('\nEscribe una palabra pata traducirla a Pig Latin: ')
    traduccion = traductor(palabra)

    print(f'\n{palabra} en pig latin = {traduccion}')