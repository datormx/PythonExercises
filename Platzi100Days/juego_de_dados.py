import random

def generate_dices(number_of_dices):
    dices = []
    for _ in range(number_of_dices):
        dices.append([1, 2, 3, 4, 5, 6])

    return dices


def throw_dices(dices):
    throws = []
    for dice in dices:
        throw = random.choice(dice)
        # print(throw)
        throws.append(throw)    
    score = sum(throws)

    return (throws, score)


def select_winner(scores):
    if scores[0] > scores[1] and scores[0] > scores[2]:
        print('PLAYER 1 WON!!!')
    elif scores[1] > scores[0] and scores[1] > scores[2]:
        print('PLAYER 2 WON!!!')
    elif scores[2] > scores[0] and scores[2] > scores[1]:
        print('PLAYER 3 WON!!!')        
    elif scores[0] == scores[1] and scores[0] == scores[2]:
        print('ALL PLAYERS ARE TIED.')
    elif scores[0] == scores[1]:
        print('Player 1 and Player 2 are TIED.')
    elif scores[1] == scores[2]:
        print('Player 2 and Player 3 are TIED.')
    elif scores[0] == scores[2]:
        print('Player 1 and Player 3 are TIED.')
    

def run():
    print('3 players will throw 2 dices each. The one with the highest score wins!\n')

    players = []
    for player in range(3):
        dices = generate_dices(2)       
        results, score = throw_dices(dices)
        players.append(score)
        
        print(f'\nPLAYER {player+1}')
        print(f'Dices thrown: {results}.')
        print(f'Score: {score}.\n')

    winner = select_winner(players)


if __name__ == "__main__":
    run()