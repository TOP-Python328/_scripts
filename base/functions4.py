# все параметры — позиционно-ключевые
def calculator(num1: int, num2: int, operation: str) -> int | float:
    """Возвращает результат математической операции для двух чисел. Символ операции передаётся в operation."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return float(f"{'' if num1 >= 0 else '-'}inf")


# >>> calculator(4, 6, '-')
# -2
# >>> calculator(4, 6, operation='-')
# -2
# >>> calculator(num1=4, num2=6, operation='-')
# -2
# >>> calculator(operation='-', num2=4, num1=6)
# 2
# >>>
# >>> calculator(operation='-', 4, 6)
# ...
# SyntaxError: positional argument follows keyword argument
# >>>
# >>>
# >>> calculator(10, operation='*', num2=5)
# 50
# >>> 
# >>> calculator(10, operation='*', num1=5)
# ...
# TypeError: calculator() got multiple values for argument 'num1'
