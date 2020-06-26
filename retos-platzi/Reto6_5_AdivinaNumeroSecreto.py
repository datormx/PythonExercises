from random import randint

secret_number = randint(1, 100)
answer = 0
n = 0

while answer != secret_number:
    answer = int(input('\nWhich number was randomly selected? '))
    n += 1
    if answer > secret_number:
        print('Your number is bigger.')
    elif answer < secret_number:
        print('Your number is smaller.')

print(f'\nCORRECT!. The secret number is {answer}')
print(f'Number of attempts: {n}')