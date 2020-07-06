def area_triangulo(b, h):
    area = (b * h) / 2

    return area

if __name__ == "__main__":
    base = float(input('Ingresa la base del triángulo: '))
    altura = float(input('Ingresa la altura del triángulo: '))

    result = area_triangulo(base, altura)

    print(f'\n\tEl área del triángulo es: {result}')