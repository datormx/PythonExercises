
decimals = int(input('How many decimals do you need in the result?: '))
num_1 = float(input('Insert first number (use two or more decimals): '))
num_2 = float(input('Insert second number (use two or more decimals): '))

multiplication = num_1 * num_2

print(f'{num_1} * {num_2} = {round(multiplication, decimals)}')