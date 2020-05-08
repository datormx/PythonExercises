if __name__ == "__main__":
    miles = float(input('Write a numer of miles to convert them to kilometers: '))

    kilometers = round(miles * 1.609344, 4)

    print(f'{miles} miles are {kilometers} kilometers')