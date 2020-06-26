number_1 = int(input('Insert a number: '))
number_2 = int(input('Insert other number: '))
answer = 'yes'
addition = number_1 + number_2

while answer == 'yes':
    answer = input('Do you want to add another number? YES/NO ')
    answer.lower()
    if answer == 'yes':
        number = int(input('Insert number: '))
        addition += number
    
print(f'Total = {addition}')

