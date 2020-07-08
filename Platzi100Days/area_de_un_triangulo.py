def area_triangulo(b, h):
    """Calcula el área de un triángulo

    Parámetros:
    b, h float > 0

    Retorna:
    area = (b * h) / 2 float > 0"""

    area = (b * h) / 2

    return area


def triangle_type(b, h):
    """Dependiendo de los valores de base y altura decide
    si un triángulo es escaleno, isósceles o equilatero.

    Parámetros:
    b, h float > 0

    Retorna:
    triangle_t string"""

    triangle_t = 'equilatero'

    if b < h:
        triangle_t = 'isósceles'
    elif b > h:
        triangle_t = 'escaleno'

    return triangle_t


if __name__ == "__main__":
    base = float(input('Ingresa la base del triángulo: '))
    altura = float(input('Ingresa la altura del triángulo: '))

    triangle = triangle_type(base, altura)
    result = area_triangulo(base, altura)

    print(f'\n\tEl triángulo es {triangle}.')
    print(f'\tEl área del triángulo es: {result}')