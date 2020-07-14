def ppt(choice_player1, choice_player2):
    """Determina qué jugador gana en una partida de piedra, papel o tijeras

    Parámetros
    choice_player1, choice_player2 int de 1 a 3

    Retorna
    Jugador ganador de la partida
    int 1 o 2"""
    
    if choice_player1 == choice_player2:
        return None

    elif choice_player1 == 1 and choice_player2 == 3: #Piedra > Tijeras
        return 1
    elif choice_player2 == 1 and choice_player1 == 3:
        return 2

    elif choice_player1 == 2 and choice_player2 == 1: #Papel > Piedra
        return 1
    elif choice_player2 == 2 and choice_player1 == 1: 
        return 2

    elif choice_player1 == 3 and choice_player2 == 2: #Tijeras > Papel
        return 1
    elif choice_player2 == 3 and choice_player1 == 2: 
        return 2


if __name__ == "__main__":

    ganadores = []
    for _ in range(3):

        print("""Elige tu mano:
        [1] Piedra
        [2] Papel
        [3] Tijeras
        """)

        mano_jugador1 = int(input('Jugador 1: '))
        mano_jugador2 = int(input('Jugador 2: '))
        ganador = ppt(mano_jugador1, mano_jugador2)
        ganadores.append(ganador)
    # print(ganadores)

    veces_ganadas_jugador1 = ganadores.count(1)
    veces_ganadas_jugador2 = ganadores.count(2)

    # print(veces_ganadas_jugador1, veces_ganadas_jugador2)
    if veces_ganadas_jugador1 > veces_ganadas_jugador2:
        print(f'\nEl ganador es el Jugador 1 con {veces_ganadas_jugador1} partidas ganadas.')
    elif (veces_ganadas_jugador2 > veces_ganadas_jugador1):
        print(f'\nEl ganador es el Jugador 2 con {veces_ganadas_jugador2} partidas ganadas.')
    elif (veces_ganadas_jugador1 == veces_ganadas_jugador2):
        print('\nEs un empate.')  