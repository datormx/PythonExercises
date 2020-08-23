def interes(monto, meses):
    monto_con_intereses = monto
    for _ in range(meses):        
        interes = monto_con_intereses * 0.04
        monto_con_intereses += interes  

    monto_con_intereses = round(monto_con_intereses, 2)

    return monto_con_intereses


def run():
    continuar = True
    while continuar:
        ahorro_inicial = float(input('\n¿Con qué cantidad iniciarás tus ahorros?: '))
        meses = int(input('¿Por cuántos meses ahorrarás tu dinero?: '))
        ahorro_con_intereses  = interes(ahorro_inicial, meses)
        print(f"""\nAl comenzar a ahorrar ${ahorro_inicial} hoy tendrás en:
        {meses} meses: ${ahorro_con_intereses}
        """)

        seguir = input('¿Desea agregar otra cantidad de ahorro inicial? (S/N) ')
        seguir = seguir.lower()
        if seguir == 'n':
            continuar = False


if __name__ == "__main__":
    run()