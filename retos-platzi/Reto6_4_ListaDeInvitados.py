answer = 'yes'
guests = []
total_guests = 0
print('YOUR BIRTHDAY GUEST LIST. Add your guests.')


while answer == 'yes':
    friend = input('Insert your friend\'s name: ')
    guests.append(friend)
    total_guests += 1
    answer = input('Do you want to add another friend to your guest list? YES/NO ')
    answer.lower()

print(f'\nYou invited {total_guests} guests to your party.')
print('Your friends are: ')
for guest in guests:
    print(guest)


