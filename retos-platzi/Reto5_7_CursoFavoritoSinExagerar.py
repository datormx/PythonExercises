curso = input('Which is your favorite Platzi Course? ')
n = int(input('How many times do you want to print the course? '))

if n <= 0: 
    print('ERROR: You entered 0 or a negative number when asked how many times do you want to print the course.')
elif n > 15:
    for _ in range(3):
        print(curso)
    print(f'Sorry {n} is a big number. I can\'t print so many times.')
else:
    for _ in range(n):
        print(curso)