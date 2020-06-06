from math import pi

def circle_area(r):
    return pi * (r**2)


def cilinder_volume(r, h):
    return circle_area(r) * h


if __name__ == "__main__":
    radius = float(input('Insert the circle radius: '))
    height = float(input('Insert the height of the cilinder: '))

    volume = cilinder_volume(radius, height)
    print(f'Volume = {volume}')