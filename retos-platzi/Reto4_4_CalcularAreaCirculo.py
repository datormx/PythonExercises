from math import pi

radius = float(input('Insert the circle radius: '))

area = pi * (radius**2)
area = round(area, 5)

print(f'Circle area = {area}')