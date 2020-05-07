if __name__ == "__main__":
    x_pizza = int(input('How many pizza slices did you bring?  '))
    y_pizza = int(input('How many pizza slices did you eat? '))
    z_pizza = x_pizza - y_pizza


    print(f'\nYou brought {x_pizza} slices')
    if y_pizza == (x_pizza - 2) or y_pizza == x_pizza:
        print(f'YOU ATE {y_pizza} SLICES! (That\'s too much pizza. ;) JK')
        print(f'Now there are only {z_pizza} slices left for breakfast')

    elif y_pizza < x_pizza - 2:
        print(f'You ate {y_pizza} slices. (Nice, keeping a good diet)')
        print(f'Now there are only {z_pizza} slices left.')

    elif y_pizza > x_pizza:
        print(f'Liar, you couldn\'t have eaten {y_pizza} slides if you only brought {x_pizza} slices.')




