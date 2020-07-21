from math import pi

def volumen_cilindro(r, h):
    return pi*(r**2)*h


def volumen_cubo(l):
    return l**3


def volumen_esfera(r):
    return (pi*(r**3)*4)/3


def run():
    menu = """Calculadora de volúmenes: Cubo, esfera y cilindro:
    [C]ubo
    [E]sfera
    [Ci]lindro

    Inserta las letras de la figura a calcular: """

    opcion = input(menu)
    opcion = opcion.lower()    

    if opcion == 'c':
        figura = 'cubo'
        lado = float(input('\n\nInserta el tamaño del lado del cubo: '))
        volumen = volumen_cubo(lado)
    elif opcion == 'e':
        figura = 'esfera'
        radio = float(input('\n\nInserta el tamaño del radio de la espera: '))
        volumen = volumen_esfera(radio)
    elif opcion == 'ci':
        figura = 'cilindro'
        radio = float(input('\n\nInserta el tamaño del radio del cilindro: '))
        altura = float(input('\n\nInserta el tamaño de la altura del cilindro: '))
        volumen = volumen_cilindro(radio, altura)
        
    volumen = round(volumen, 1)
    print(f'\nEl volumen de la figura {figura} es {volumen} unidades cúbicas.')


if __name__ == "__main__":
    run()