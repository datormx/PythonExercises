import random
numbers = [1, 2, 3, 4, 5, 6]


def generate_dices(number_of_dices):
    dices = []
    for _ in range(number_of_dices):
        dice = random.choice(numbers)
        dices.append(dice)
    
    return dices


def compare_players(dices_1, dices_2):
    dices_1.sort(reverse = True)
    dices_2.sort(reverse = True)

    print(f'Attacker dices: {dices_1}')
    print(f'Defender dices: {dices_2}')

    challenge_1 = dices_1[0] - dices_2[0]
    challenge_2 = dices_1[1] - dices_2[1]

    return challenge_1, challenge_2


def select_looser(result):
    if result == 0:
        message = "Tie."
    elif result > 0:
        points = abs(result)
        message = f'Defender looses {points} points.'
    elif result < 0:
        points = abs(result)
        message = f'Attacker looses {points} points.'
        
    return message


def run():
    player_1_dices = generate_dices(3)
    player_2_dices = generate_dices(2)
    result_1, result_2 = compare_players(player_1_dices, player_2_dices)
    winner1 = select_looser(result_1)
    winner2 = select_looser(result_2)
    print(winner1)
    print(winner2)

if __name__ == "__main__":
    run()