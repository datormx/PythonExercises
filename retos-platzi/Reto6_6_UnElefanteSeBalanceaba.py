elefants = 1
answer = 0

while elefants < 10:
    if elefants == 1:
        print(f"""\n
        {elefants} elefante se balanceaba
        Sobre la tela de una araña
        Como veía que resistía
        Fue a llamar otro elefante""")
    elif elefants > 1:
        print(f"""\n
        {elefants} elefantes se balanceaban
        Sobre la tela de una araña
        Como veían que resistían
        Fueron a llamar otro elefante""")
    
    while answer != elefants + 1:
        answer = int(input('\n¿Cuántos elefantes más se balancearán? '))
        if answer != elefants + 1:
            print('¡INTENTA DE NUEVO!')
    
    elefants = answer

print('FIN')