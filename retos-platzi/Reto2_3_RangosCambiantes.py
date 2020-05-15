# Nuevamente pide a tu usuario que indique 3 números: un límite superior, un límite inferior y uno de comparación. 
# Si el número de comparación se encuentra entre los 2 primeros, comunicarlo en pantalla. 
# En caso estar por debajo del límite inferior o por arriba del límite superior, también mostrarlo en pantalla.

def within_range(number, lower_limit, higher_limit):
    if number < higher_limit and number > lower_limit:
        print(f'\nThe number {number} is within range.')
    elif number > higher_limit:
        print(f'\nYour number {number} exceeds the higher limit {higher_limit}')
    elif number < lower_limit:
        print(f'\nYour number {number} does not reach the lower limit {lower_limit}')


if __name__ == "__main__":
    print('**I will tell you if your number is within range**')

    lower_limit = int(input('Lower limit: '))
    higher_limit = int(input('Higher limit: '))
    
    if lower_limit < higher_limit:
        number = int(input('Number: '))
        within_range(number, lower_limit, higher_limit)
    else:
        print('Those limits are not correct. The higher limit is lower than the lower limit or both are equal')
        print('TRY AGAIN, PLEASE')

    