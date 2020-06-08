def ack(m, n):
    """Computes de Ackermann function A(m, n)

    n, m int > 0
    """

    if m == 0:
        return n + 1

    if n == 0:
        return ack(m - 1, 1)

    return ack(m - 1, ack(m, n - 1))


print(ack(3, 4))

    