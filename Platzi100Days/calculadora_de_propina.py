def calcular_subtotal(cantidad_platillos):
    valores = []

    for _ in range(cantidad_platillos):
        valor = float(input('Ingresa el costo del platillo o producto: '))
        valores.append(valor)
    subtotal = sum(valores)
    return subtotal


def calculadora_propipna(subtotal, porcentaje_propina):
    porcentaje_propina /= 100
    propina_calculada = subtotal * porcentaje_propina
    propina_calculada = round(propina_calculada, 2)

    return propina_calculada


def calculadora_total(subtotal, propina, porcentaje_impuesto):
    porcentaje_impuesto /= 100
    total_sin_impuestos = subtotal + propina
    impuestos = total_sin_impuestos * porcentaje_impuesto
    total = total_sin_impuestos + impuestos
    total = round(total, 2)

    return total


def main():
    numero_platillos = int(input('\nIngresa la cantidad de platillos y o productos: '))
    if numero_platillos > 0:
        subtotal_platillos = calcular_subtotal(numero_platillos)
        print(f'Subtotal: {subtotal_platillos}')

        porc_propina = int(input('\nIngresa el porcentaje de propina: '))
        propina = calculadora_propipna(subtotal_platillos, porc_propina)
        print(f'\nPropina: {propina}')

        porc_impuesto = int(input('\nIngresa el porcentaje de impuesto en tu región: '))
        total = calculadora_total(subtotal_platillos, propina, porc_impuesto)
        print(f'\nTotal: {total}')
    else: 
        print('\n\tIngresaste una cantidad de platillo no válida. Ingresa 1 o más platillos.')
        main()



if __name__ == "__main__":
    main()