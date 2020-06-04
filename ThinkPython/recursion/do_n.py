def do_n(func, n):
    """Executes the a function n times
    func function object
    n int>0
    """

    if n <= 0:
        return
    else:
        func()
        do_n(func, n - 1)

    
def print_hello():
    print('hello!')

print(print_hello)
print(type(print_hello))
do_n(print_hello, 6)