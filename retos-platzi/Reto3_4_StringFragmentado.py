if __name__ == "__main__":
    long_text = input('Write your favorite song lyrics or poem: ')
    print('\nThe next numbers must not exceed the lenght of your past text.')
    minor_interval = int(input('Write the inferior limit: '))
    mayor_interval = int(input('Write the superior limit: '))
    print('\nGreat, printing that part of your text..\n')

    print(long_text[minor_interval:mayor_interval + 1]) #Using slice notation to manipulate the string



