from math import sqrt

number = int(input('Insert a number: '))
decimals = int(input('How many decimals do you need in the result?: '))

square_root = round(sqrt(number), decimals)

print(f'The square root of {number} = {square_root}')