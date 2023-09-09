def gcd(number1: int, number2: int) -> int:
    """Рекурсивная реализация нахождения наибольшего общего делителя (НОД)."""
    if number2 > 0:
        res = gcd(number2, number1 % number2)
        return res
    else:
        return number1


# >>> gcd(12, 6)
# 6
# >>> gcd(15, 12)
# 3

