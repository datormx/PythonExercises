def hypotenuse(a, b):
    """Calculates the hypotenuse of a triangle

    a int > 0
    b int > 0

    returns a**2 + b**2
    """

    a_sq = a**2
    b_sq = b**2
    c = a_sq + b_sq

    return c


print(hypotenuse(3, 4))