def is_triangle(lenght_1, lenght_2, lenght_3):
    if lenght_1 > lenght_2 + lenght_3:
        return False
    elif lenght_2 > lenght_1 + lenght_3:
        return False
    elif lenght_3 > lenght_1 + lenght_2:
        return False
    else:
        return True


def main():
    len_1 = int(input('Insert the lenght of the first stick: '))
    len_2 = int(input('Insert the lenght of the second stick: '))
    len_3 = int(input('Insert the lenght of the third stick: '))

    result = is_triangle(len_1, len_2, len_3)

    if result:
        print('Yes')
    else: 
        print('No')


if __name__ == "__main__":
    main()


