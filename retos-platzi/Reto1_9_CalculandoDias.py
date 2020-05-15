if __name__ == "__main__":
    day_amount = int(input('Write a number of days: '))

    hours = day_amount * 24
    minutes = day_amount * 1440
    seconds = day_amount * 86400

    print(f'{day_amount} day(s) are {hours} hours')
    print(f'{day_amount} day(s) are {minutes} minutes')
    print(f'{day_amount} day(s) are {seconds} seconds')