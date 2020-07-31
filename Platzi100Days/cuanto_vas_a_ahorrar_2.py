def interes(monto, meses):
    monto_con_intereses = monto
    for _ in range(meses):        
        interes = monto_con_intereses * 0.04
        monto_con_intereses += interes  

    monto_con_intereses = round(monto_con_intereses, 2)

    return monto_con_intereses


def run():
    ahorro_inicial = float(input('¿Con qué cantidad iniciarás tus ahorros?: '))
    meses = int(input('¿Por cuántos meses ahorrarás tu dinero?: '))
    ahorro_con_intereses  = interes(ahorro_inicial, meses)
    print(f"""\nAl comenzar a ahorrar hoy ${ahorro_inicial} tendrás en:
    {meses} meses: ${ahorro_con_intereses}
    """)


if __name__ == "__main__":
    run()