def repite_palabra(palabra, veces, string_repetido = ''):
        if veces == 0:
            return string_repetido

        string_repetido += palabra + ' '
        return repite_palabra(palabra, veces - 1, string_repetido)


if __name__ == "__main__":
    cadena = repite_palabra("Platzi", 5)
    print(cadena)