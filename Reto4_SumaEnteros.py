if __name__ == "__main__":
    print('Welcome, sum 2 numbers with a precision of 4 decimals')
    num_1 = round(float(input('\nWrite a number: ')), 4)
    num_2 = round(float(input('Write a second number: ')), 4)
    addition = num_1 + num_2
    print(f'\nThe sum {num_1} + {num_2} = {addition}')
