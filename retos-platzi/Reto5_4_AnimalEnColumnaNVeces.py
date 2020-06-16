animal = input('Animal: ')
n = int(input('How many times do you want to print the animal? '))

for _ in range(n):
    for letter in animal:
        print(letter)
    print('\n')
    