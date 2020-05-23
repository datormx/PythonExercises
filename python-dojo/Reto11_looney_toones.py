toonie = 200
loonie = 100
quarter = 25
dime = 10
nickel = 5
pennies = 1

cents = int(input('How many cents do you have? '))

print(f'{cents//toonie} toonies')
cents = cents % toonie

print(f'{cents//loonie} loonies')
cents = cents % loonie

print(f'{cents//quarter} quarters')
cents = cents % quarter

print(f'{cents//dime} dimes')
cents = cents % dime

print(f'{cents//nickel} nickels')
cents = cents % nickel

print(f'You got {cents} pennies')