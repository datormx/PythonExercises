import random

if __name__ == "__main__":
    print('Write two words, one will be printed randomly in mayus and the other in minus.')
    word_1 = input('First word: ')
    word_2 = input('Second word: ')

    word_selected_for_mayus = random.choice([word_1, word_2])    

    if word_selected_for_mayus == word_1:
        print(word_selected_for_mayus.upper())
        print(word_2.lower())
    elif word_selected_for_mayus == word_2:
        print(word_1.lower())
        print(word_selected_for_mayus.upper())