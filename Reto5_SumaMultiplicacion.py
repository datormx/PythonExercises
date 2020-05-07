if __name__ == "__main__":
    print('Welcome, sum the first two numbers, then multiply the result by a third number.\
        \n\n**The numbers will only have 4 decimals.')
    num_1 = round(float(input('\nWrite a number: ')), 4)
    num_2 = round(float(input('Write a second number: ')), 4)
    num_3 = round(float(input('Write a third number: ')), 4)
    print(f'Number data: {num_1}, {num_2}, {num_3}')

    operation = num_1 + num_2
    operation *= num_3
    print(f'Result = {operation}')

