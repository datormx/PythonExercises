# Crearás un un script para el que el usuario indicará un número entre 1 y 6. 
# Como respuesta se le brindará un mensaje según el número leido:
# 1 - “Hoy aprenderemos sobre prorgamación”
# 2 - “¿Qué tal tomar un curso de marketing digital?
# 3 - “Hoy es un gran día para comenzar a aprender de diseño”
# 4 - ¿Y si aprendemos algo de negocios online?
# 5 - “Veamos un par de clases sobre producción audiovisual”
# 6 - “Tal vez sea bueno desarrollar una habilidad blanda en Platzi”
# En caso indicar un número distinto, pedir al usuario que ingrese uno en el rango válido.


if __name__ == "__main__":
    print('**Select a number to know what\'s ahead in your future**')

    number = int(input('Insert a number from 1 to 6: '))

    if number == 1:
        print('Today we will learn programming')
    elif number == 2:
        print('How about taking a digital marketing course?')
    elif number == 3:
        print('Today is a great day to start learning design')
    elif number == 4:
        print('What if we learn online business?')
    elif number == 5:
        print('Let\'s watch some classes of video production')
    elif number == 6:
        print('Maybe it\'s a great time to develop a soft skill in Platzi')
    else:
        print('\nThe number you inserted is not valid. Try again, please.')