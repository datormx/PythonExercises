import math

def square_root(a):

    x = 3.0
    epsilon = 0.00000001

    while True:
        # print(x)
        y =(x + (a/x)) / 2    
        if abs(y-x) < epsilon:
            break
        x = y

    return y


def test_square_root(a):
    calculated_sqrt = square_root(a)
    math_sqrt = math.sqrt(a)
    absolute_difference = abs(calculated_sqrt - math_sqrt)

    print(f'{a}       |       {calculated_sqrt}       |       {math_sqrt}     |       {absolute_difference}')

if __name__ == "__main__":   

    print('Number       |       calculated_sqrt       |       math_sqrt     |       absolute_difference')
    for number in range(1,11):
        test_square_root(number)