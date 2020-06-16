option = input('Do you want a negative or positive number line: ')
option = option.lower()
number = int(input('Number: '))
number_line = []

if option == 'positive':
    if number > 0:
        for num in range(number + 1):
            number_line.append(num)
    else:
        print('NUMBER NOT POSITIVE')
elif option == 'negative':
    if number < 0:
        for num in range(number, 1):
            number_line.append(num)
    else:
        print('NUMBER NOT NEGATIVE')

print(number_line)



