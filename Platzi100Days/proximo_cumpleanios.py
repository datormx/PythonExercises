from datetime import date

hoy = date.today()


if __name__ == "__main__":
    dia = int(input('\nEscribe tu día de nacimiento: '))
    mes = int(input('Escribe tu mes de nacimiento: '))
    anio = int(input('Escribe tu año de nacimiento: '))

    fecha_nacimiento = date(anio, mes, dia)
    cumpleanos_anio_actual = date(hoy.year, fecha_nacimiento.month, fecha_nacimiento.day)

    if cumpleanos_anio_actual > hoy:
        delta = cumpleanos_anio_actual - hoy
        
    else: 
        cumpleanos_anio_siguiente = date(hoy.year + 1, fecha_nacimiento.month, fecha_nacimiento.day)
        delta = cumpleanos_anio_siguiente - hoy

    print(f'\n\nFaltan {delta.days} días para tu cumpleaños.')