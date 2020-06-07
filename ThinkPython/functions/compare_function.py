def compare_function(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1


if __name__ == "__main__":
    x = 7
    y = 5
    result = compare_function(x, y)

    if result == 1:
        print(f'{x} > {y}')
    elif result == 0:
        print(f'{x} == {y}')
    elif result == -1:
        print(f'{x} < {y}')