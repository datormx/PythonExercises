if __name__ == "__main__":
    big_number = int(input('Write a number bigger than 1000: '))
    small_number = int(input('Write a number smaller than 100: '))

    times_small_in_big = big_number // small_number

    print(f'The number {small_number} fits {times_small_in_big} times in {big_number}')