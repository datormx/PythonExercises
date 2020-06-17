def gcd(a, b):
    """Calculates the greatest common divisor among a and b
    
    Parameters: a, b int > 0

    return: The value of a and b greatest common divisor
    """
    print(a, b)
    if b == 0:
        return a

    r = a % b
    
    return gcd(b, r)

result = gcd(20, 100)
print(f'gcd = {result}')
    