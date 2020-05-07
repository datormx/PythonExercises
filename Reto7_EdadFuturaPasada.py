if __name__ == "__main__":
    print('Welcome, you will know how old were you last years and how old you are going to be next year.')

    name = input('Write your name: ')
    age = int(input('Write your age: '))
    f_age = age + 1
    p_age = age - 1

    print(f'{name}, you were {p_age} years old last year and you will be {f_age} next year.')