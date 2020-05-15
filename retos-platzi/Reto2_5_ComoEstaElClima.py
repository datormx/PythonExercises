# Crea un programa que pregunte al usuario si está lloviendo, en caso de responder “sí” pregunta si está 
# haciendo mucho viento y si responde “sí” nuevamente muestra un mensaje indicando que hace mucho viento 
# para salir con una sombrilla. En caso contrario, anima al usuario a que lleve una sombrilla. 
# Para el caso de responder “no” en la primer pregunta, entonces solo desea un bonito día.
# Considera que las respuestas pueden pasarse a minúsculas para evitar posibles errores.

if __name__ == "__main__":
    is_raining = input('Is it raining today? (Yes/No) ')
    is_raining = is_raining.lower()

    if is_raining == 'yes':
        is_wind = input('Is there a lot of wind? (Yes/No) ')        
        is_wind = is_wind.lower()

        if is_wind == 'yes':
            print('\nThere\'s too much wind outside. An umbrella won\'t be enough.')
        elif is_wind == 'no':
            print('\nYou should go outside with an umbrella.')
        else:
            print('\nYou did not insert an adequate answer. Try again with \"Yes\" or \"No\"')

    elif is_raining == 'no':
        print('\nHave a nice day! :-)')
    else:
        print('\nYou did not insert an adequate answer. Try again with \"Yes\" or \"No\"')
