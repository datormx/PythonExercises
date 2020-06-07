from math import sqrt

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


print(distance(1, 2, 4, 6))