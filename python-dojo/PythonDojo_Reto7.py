if __name__ == "__main__":
    number = int(input('Please choose a number to sum it: '))
    # (n)(n + 1) / 2

    result = ((number)*(number + 1)) / 2

    print(f'The progressive sum of {number} is {int(result)}')