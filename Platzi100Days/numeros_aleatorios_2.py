import random

def generate_dices(number_of_dices, number_of_faces):
    dices = []
    faces = [face + 1 for face in range(number_of_faces)]
    # print(faces)

    for _ in range(number_of_dices):        
        dices.append(faces)

    return dices


def throw_dices(dices):
    throws = []
    for dice in dices:
        throw = random.choice(dice)
        # print(throw)
        throws.append(throw)    
    score = sum(throws)

    return (throws, score)


def run():
    dices_amount = int(input('How many dices will you throw? '))
    dice_faces = int(input('How many faces will your dices have? '))
    dices = generate_dices(dices_amount, dice_faces)
    results, final_score = throw_dices(dices)

    print(f'\nDices thrown: {results}.')
    print(f'Final score: {final_score}.')

if __name__ == "__main__":
    run()