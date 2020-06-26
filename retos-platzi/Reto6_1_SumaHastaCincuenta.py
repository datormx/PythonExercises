total = 0
n = 0
addition = int(input('Insert a number to add to the total: '))

while total <= 50:
    total += addition
    n+=1

print(f'Result = {total}')
print(f'The while loop iterated {n} times.')
