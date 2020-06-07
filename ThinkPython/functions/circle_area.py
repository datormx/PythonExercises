from math import pi, sqrt

def circle_area(xc, yc, xp, yp):
    """Calculates the area of a circle given the center point of the circle and
    a point in the circle's perimeter

    xc int >= 0
    yc int >= 0
    xp int >= 0
    yp int >= 0

    returns area(distance(xc, yc, xp, yp))
    """
    distance_c_p = distance(xc, yc, xp, yp)
    result = area(distance_c_p)

    return result


def distance(x1, y1, x2, y2):
    """Calculates the distance between two points x and y.

    x1 int >= 0
    y1 int >= 0
    x2 int >= 0
    y2 int >= 0

    returns sqrt((x2 - x1)**2 + (y2 - y1)**2)
    """
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = sqrt(dsquared)
    return result


def area(r):
    """Calculates the area of a circle given the radius

    r int > 0

    returns pi*(r**2)
    """
    return pi*(r**2)


print(circle_area(1, 2, 4, 6))