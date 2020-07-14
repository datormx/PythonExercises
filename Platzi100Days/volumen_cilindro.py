from math import pi

def area_circulo(r):
    area = pi*(r**2)

    return area


def volumen_cilindro(a, h):
    volumen = a * h

    return volumen


if __name__ == "__main__":
    print("Cálculo de volumen de cilindro")

    radio = float(input("\nIngresa el radio del círculo base: "))
    altura = float(input("Ingresa la altura del cilindro: "))
    area = area_circulo(radio)
    volumen = volumen_cilindro(area, altura)
    volumen = round(volumen, 1)

    print(f'\nVolumen del cilindro = {volumen} unidades cúbicas')