def prime_numbers(n, memory = {}):
    number = 0
    position = 1
    while len(memory) < n:
        result = is_prime(number, memory)
        if result:
            memory[number] = position
            position += 1
        number += 1        

    return memory


def is_prime(number, memory):
    count = 0

    if number <= 1:
        return False    

    for i in range(1, number + 1):     
        if i == 1 or i == number:
            continue   
        if number % i == 0:
            count += 1
            break
    if count == 0:
        return True
    else:
        return False


def run():

    n = int(input('Insert a number: '))
    results = prime_numbers(n)
    print(results)


if __name__ == "__main__":
    run()


