import sys

def fibonacci(n, memory = {}):
    if n == 1 or n == 2:
        return 1

    try: 
        return memory[n]
    except KeyError:
        resultado = fibonacci(n - 1, memory) + fibonacci(n - 2, memory)
        memory[n] = resultado

    return resultado


def run():
    n = 9567
    result = fibonacci(9567)
    print(f'Fibonacci of {n} = {result}')


if __name__ == "__main__":
    sys.setrecursionlimit(10002)
    run()