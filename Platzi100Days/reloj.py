def convert_to_seconds(days = 0, hours = 0, minutes = 0):
    """Convierte días, horas, minutos en segundos.

    Parámetros:
    days, hours, minutes int >= 0

    Retorna:
    Suma de conversiones de los parámetros a segundos 
    seconds int>=0"""

    s_days = days * 86400
    s_hours = hours * 3600
    s_minutes = minutes * 60

    seconds = s_days + s_hours + s_minutes
    print(seconds)

    return seconds

if __name__ == "__main__":
    dias = int(input('Inserta el número de días: '))
    horas = int(input('Inserta el número de horas: '))
    minutos = int(input('Inserta el número de minutos: '))

    result = convert_to_seconds(dias, horas, minutos)

    print(f'{dias} días, {horas} horas y {minutos} minutos son {result} segundos.')
