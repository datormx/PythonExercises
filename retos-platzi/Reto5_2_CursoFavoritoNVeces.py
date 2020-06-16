curso = input('Which is your favorite Platzi Course? ')
n = int(input('How many times do you want to print the course? '))

if n <= 0: 
    print('ERROR: You entered 0 or a negative number when asked how many times do you want to print the course.')
else:
    for _ in range(n):
        print(curso)