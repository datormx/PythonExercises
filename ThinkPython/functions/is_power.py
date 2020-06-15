def is_power(a, b):
    """Checks if a is a power o b

    a, b int > 0, a > b

    returns True if a is a power of b
    """
    if (a / b) == b:
        return True
    
    if a % b == 0:
        c = a / b
        return is_power(c, b)

    return False


print(is_power(25, 5))