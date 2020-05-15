# Escribe un programa que pida al usuario ingrese su animal favorito, si coloca ‘Tortuga’, 
# ‘tortuga’, ‘TORTUGA’ o cualquier otra variante de la palabra entonces mostrar en pantalla 
# “También me gustan las tortugas”. En caso contrario mostrar el mensaje “Ese animal es genial, pero prefiero las tortugas”.

if __name__ == "__main__":
    animal = input('Which is your favorite animal? ')

    animal_lower_case = animal.lower()

    if animal_lower_case == 'turtle' or animal_lower_case == 'tortuga':
        print('\nI like turtles too')
    else:
        print('\nThat animal is great, but I prefer turtles.')

