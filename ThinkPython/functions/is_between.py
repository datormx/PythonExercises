def is_between(x, y, z):
    return x <= y and y <= z

x = 4
y = 9
z = 7

if is_between(x, y, z):
    print(f'{y} is between {x} and {z}')
else:
    print(f'{y} is not between {x} and {z}')