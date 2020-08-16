import math

def calculate_x(a, b, c):
    discriminant = (b**2) - (4*a*c)
    minus_b = -b
    divisor = 2*a

    if discriminant > 0:
        x1 = (minus_b + math.sqrt(discriminant))/divisor
        x2 = (minus_b - math.sqrt(discriminant))/divisor      

    elif discriminant == 0:
        x1 = (minus_b)/divisor
        x2 = x1

    elif discriminant < 0:
        x1 = f'{minus_b / divisor} + {math.sqrt(abs(discriminant))/divisor}i'
        x2 = f'{minus_b / divisor} - {math.sqrt(abs(discriminant))/divisor}i'

    return (x1, x2)


def run():
    print('C U A D R A T I C  E Q U A T I O N\n')
    a = int(input('Insert a: '))
    b = int(input('Insert b: '))
    c = int(input('Insert c: '))

    assert a != 0, 'a must not be 0'

    x1, x2 = calculate_x(a, b, c)
    print(f'x1 = {x1}, x2 = {x2}')


if __name__ == "__main__":
    run()