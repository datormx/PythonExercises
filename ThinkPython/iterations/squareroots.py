
def square_root(a):

    x = 3.0
    epsilon = 0.00000001

    while True:
        print(x)
        y =(x + (a/x)) / 2    
        if abs(y-x) < epsilon:
            break
        x = y

    return y


if __name__ == "__main__":
    value = int(input('Insert value to calculate sqr root: '))

    result = square_root(value)
    print(f'The square root of {value} is {result}')