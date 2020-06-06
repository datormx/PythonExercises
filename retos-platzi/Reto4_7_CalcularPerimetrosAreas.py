from math import pi

def circle_area(r):
    return pi * (r**2)


def circle_perimeter(r):
    return 2 * pi * r


def polygon_perimeter(s, number_of_sides):
    return s * number_of_sides


def square_area(s):
    return s * s


def triangle_area(b, h):
    return (b * h) / 2


def rectangle_area(w, h):
    return w * h


def rectangle_perimeter(w, h):
    return (2 * w) + (2 * h)


def main(figure):
    if figure == 'c':
        radius = float(input('Insert the circle radius: '))

        area = circle_area(radius)
        perimeter = circle_perimeter(radius)
        print(f'Area = {area}, Perimeter = {perimeter}')

    elif figure == 's':
        n = 4
        side = float(input('Insert the square side size: '))

        area = square_area(side)
        perimeter = polygon_perimeter(side, n)
        print(f'Area = {area}, Perimeter = {perimeter}')

    elif figure == 't':
        n = 3
        base = float(input('Insert the triangle base: '))
        height = float(input('Insert the triangle height: '))

        perimeter = polygon_perimeter(base, n)
        area = triangle_area(base, height)
        print(f'Area = {area}, Perimeter = {perimeter}')

    elif figure == 'r':
        width = float(input('Insert the width of the rectangle: '))
        height = float(input('Inser the height of the rectangle: '))
        
        perimeter = rectangle_perimeter(width, height)
        area = rectangle_area(width, height)
        print(f'Area = {area}, Perimeter = {perimeter}')

        

if __name__ == "__main__":
    figure = input("""SELECT A FIGURE TO CALCULATE ITS AREA AND PERIMETER
    [C]ircle
    [S]quare
    [T]riangle
    [R]ectangle
    """)

    figure = figure.lower()

    main(figure)