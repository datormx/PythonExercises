def print_n(s, n):
    """Prints n times the string s
    s str
    n int>0
    returns print_n(s, n - 1)
    """

    if n <= 0:
        return 'end'
    else:
        print(s)
        return print_n(s, n-1)

print(print_n('Hola!', 2))