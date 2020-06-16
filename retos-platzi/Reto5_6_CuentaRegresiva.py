number = int(input('Number: '))

if number < 0:    
    for num in range(number, 1):
        print(number)
elif number > 0:
    for num in range(number + 1):
        print(number)
        number -= 1