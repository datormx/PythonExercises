number = int(input('Number: '))

for multiplier in range(11):
    if multiplier == 0:
        continue
    print(f'{number} * {multiplier} = {number * multiplier}')