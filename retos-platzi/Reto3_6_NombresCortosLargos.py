if __name__ == "__main__":
    name = input('What\'s your name? ')
    name = name.lower()

    if len(name) > 5:
        print(name.capitalize())
    elif len(name) <= 5:
        lastname = input('What\'s your lastname? ')
        lastname = lastname.lower()
        print(name.capitalize() + ' ' + lastname.capitalize())
