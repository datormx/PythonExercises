import random

def generate_dices(number_of_dices):
    dices = []
    for _ in range(number_of_dices):
        dices.append([1, 2, 3, 4, 5, 6])#Here you can modify the probability of any number (loaded dice)

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
    dices = generate_dices(dices_amount)
    results, final_score = throw_dices(dices)

    print(f'\nDices thrown: {results}.')
    print(f'Final score: {final_score}.')

if __name__ == "__main__":
    run()