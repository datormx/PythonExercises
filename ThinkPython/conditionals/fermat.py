def check_fermat(a, b, c, n):
    """
    Checks if Fermat Last Theorem is right or wront and prints it for any positive integers given
    a int > 0
    b int > 0
    c int > 0
    n int > 2
    """
    if a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn\'t work')


def main():
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    n = int(input('n: '))

    check_fermat(a, b, c, n)


if __name__ == "__main__":
    main()