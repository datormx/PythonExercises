def interes(monto):
    monto_seis_meses = monto
    for _ in range(6):        
        interes = monto_seis_meses * 0.04
        monto_seis_meses += interes
        # print(monto_seis_meses)
    
    monto_un_anio = monto_seis_meses
    for _ in range(6):        
        interes = monto_un_anio * 0.04
        monto_un_anio += interes
        # print(monto_un_anio)
    
    monto_dos_anios = monto_un_anio
    for _ in range(12):        
        interes = monto_dos_anios * 0.04
        monto_dos_anios += interes
        # print(monto_dos_anios)    

    monto_seis_meses = round(monto_seis_meses, 2)
    monto_un_anio = round(monto_un_anio, 2)
    monto_dos_anios = round(monto_dos_anios, 2)

    return monto_seis_meses, monto_un_anio, monto_dos_anios


def run():
    ahorro_inicial = 100
    ahorro_seis_meses, ahorro_un_anio, ahorro_dos_anios  = interes(ahorro_inicial)
    print(f"""\nAl comenzar a ahorrar hoy ${ahorro_inicial} tendrás en:
    6 meses: ${ahorro_seis_meses}
    1 año: ${ahorro_un_anio}
    2 años: ${ahorro_dos_anios}
    """)


if __name__ == "__main__":
    run()