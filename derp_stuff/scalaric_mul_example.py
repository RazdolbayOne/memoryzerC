def bits(n):
    """
    Генерирует двоичные разряды n, начиная
    с наименее значимого бита.

    bits(151) -> 1, 1, 1, 0, 1, 0, 0, 1
    """
    while n:
        yield n & 1
        n >>= 1


def double_and_add(n, x):
    """
    Возвращает результат n * x, вычисленный
    алгоритмом удвоения-сложения.
    """
    result = 0
    addend = x

    for bit in bits(n):
        if bit == 1:
            result += addend
        addend *= 2

    return result


print(str(double_and_add(151, 2)))
