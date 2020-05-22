if __name__ == "__main__":
    vocals = ['a', 'e', 'i', 'o', 'u']

    word = input('Write any word, it will be translated to Pig Latin: ')
    word = word.lower()

    if word[0] in vocals:
        word = word.capitalize() + 'way'
        print(word)
    else:
        word = (word[1:] + word[0] + 'ay').capitalize()
        print(word)
    
