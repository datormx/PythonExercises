def interes_banco_1(monto):
    monto_con_intereses = monto
    monto_con_intereses_2_anios = 0

    for i in range(36):        
        interes = monto_con_intereses * 0.04
        monto_con_intereses += interes  

        if i == 23:
            monto_con_intereses_2_anios = monto_con_intereses

    monto_con_intereses_2_anios = round(monto_con_intereses_2_anios, 2)
    monto_con_intereses_3_anios = round(monto_con_intereses, 2)

    return (monto_con_intereses_2_anios, monto_con_intereses_3_anios)


def interes_banco_2(monto):
    monto_con_intereses = monto
    montos_con_intereses = []

    for _ in range(3):
        for _ in range(12):        
            interes = monto_con_intereses * 0.03
            monto_con_intereses += interes

        interes_anual = monto_con_intereses * 0.07
        monto_con_intereses += interes_anual
        montos_con_intereses.append(monto_con_intereses)

    monto_con_intereses_2_anios = round(montos_con_intereses[1], 2)
    monto_con_intereses_3_anios = round(montos_con_intereses[2], 2)

    return (monto_con_intereses_2_anios, monto_con_intereses_3_anios)


def run():
    ahorro_inicial = float(input('¿Con qué cantidad iniciarás tus ahorros?: '))
    ahorro_banco_1_dos_anios, ahorro_banco_1_tres_anios = interes_banco_1(ahorro_inicial)
    ahorro_banco_2_dos_anios, ahorro_banco_2_tres_anios = interes_banco_2(ahorro_inicial)
    

    print(f"""\nAl comenzar a ahorrar hoy ${ahorro_inicial} tendrás:
    B A N C O  1
    2 años: ${ahorro_banco_1_dos_anios}
    3 años: ${ahorro_banco_1_tres_anios}

    B A N C O  2
    2 años: ${ahorro_banco_2_dos_anios}
    3 años: ${ahorro_banco_2_tres_anios}""")


if __name__ == "__main__":
    run()