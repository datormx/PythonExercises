total = 0

for _ in range(4):
    number = int(input('Number to add: '))
    option = input('Do you want to add this to total? Write Yes/No: ')
    option.lower()

    if option == 'yes':
        total += number
    
print(f'Total = {total}')
