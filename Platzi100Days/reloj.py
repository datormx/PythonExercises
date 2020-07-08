def convert_to_seconds(days, hours, minutes):
    """Convierte días, horas, minutos en segundos.

    Parámetros:
    days, hours, minutes int >= 0

    Retorna:
    Suma de conversiones de los parámetros a segundos 
    seconds int >= 0"""

    s_days = days * 86400
    s_hours = hours * 3600
    s_minutes = minutes * 60

    seconds = s_days + s_hours + s_minutes

    return seconds

if __name__ == "__main__":
    """Calcularemos cuántos segundos son dependiendo la cantidade de
    días, horas y minutos que ingreses.

    Deja vacío si no quieres introducir un valor en un campo."""

    try:
        dias = int(input(f'Inserta el número de dias: '))
    except ValueError as e:
        dias = 0

    try:
        horas = int(input('Inserta el número de horas: '))
    except ValueError as e:
        horas = 0

    try:
        minutos = int(input('Inserta el número de minutos: '))
    except ValueError as e:
        minutos = 0

    result = convert_to_seconds(dias, horas, minutos)

    print(f'\n{dias} días, {horas} horas y {minutos} minutos son {result} segundos.')
