def countdown(n):
    """Count from n to 0 and prints Blastoof when the count ends
    n int>0
    """

    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        return countdown(n-1)


countdown(10)


 