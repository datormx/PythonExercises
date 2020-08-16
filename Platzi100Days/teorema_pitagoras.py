import math

def calculate_distance(a, b):
    distance = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

    return distance


if __name__ == "__main__":
    print('P I T A G O R A S  C A L C U L A T O R\n')

    x1 = int(input('Insert coordinate x1: '))
    y1 = int(input('Insert coordinate y1: '))
    x2 = int(input('Inser coordinate x2: '))
    y2 = int(input('Insert coordinate y2: '))

    a = (x1, y1)
    b = (x2, y2)
    print(f'a = {a}')
    print(f'b = {b}')

    result = calculate_distance(a, b)
    result = round(result, 4)

    print(f'The distance between a = {a} and b = {b} is {result}')