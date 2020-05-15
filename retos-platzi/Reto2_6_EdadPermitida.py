# Pide al usuario que ingrese su edad y mostrarás un mensaje correspondiente si esta coincide con las siguientes condiciones:
# Más de 30 años: Nunca es tarde para aprender ¿Qué curso tomaremos?
# Entre 29 y 18 años: Es un momento excelente para impulsar tu carrera.
# Menos de 18 años: ¿Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte.

if __name__ == "__main__":
    age = int(input('How old are you? '))

    if age >= 30:
        print('Is never too late for learning. What course will you take today?')
    elif age <= 29 and age >= 18:
        print('It\'s a great time to boost your carreer!')
    elif age < 18:
        print('Do you know what road will you take for your future? I can help you with that.')