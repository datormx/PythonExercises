def is_divisible(x, y):
    return x % y == 0

x = 10
y = 5

if is_divisible(x, y):
    print(f'{x} is divisible by {y}')
else:
    print(f'{x} not divisible by {y}')