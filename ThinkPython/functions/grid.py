COLUMNA = '+' + '-'*4
FILA = '|    '

def draw_grid(num_col, num_filas):
    for _ in range(num_filas):
        print(COLUMNA * num_col + '+')
        for _ in range(4):
            print(FILA*(num_col + 1))
    print(COLUMNA * num_col + '+')
    

draw_grid(5,5)

