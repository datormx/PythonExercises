num_1 = int(input('Insert first number: '))
num_2 = int(input('Insert second number: '))

no_decimal_division = num_1 // num_2
module = num_1 % num_2

print(f'{num_1} divided by {num_2} is {no_decimal_division} and the residue is {module}')
