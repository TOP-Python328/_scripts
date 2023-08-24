def decorator(func_obj: 'function') -> 'function':
    """Функция-декоратор."""
    print('вызов decorator()')
    print(f'  {func_obj = }')
    print('  перед созданием функции-обёртки')
    
    def wrapper(*args, **kwargs):
        """Функция-обёртка."""
        print('    вызов wrapper()')
        print('      перед вызовом декорируемой функции')
        result = func_obj(*args, **kwargs)
        print('      после вызова декорируемой функции')
        return result
    
    print('  после создания функции-обёртки')
    return wrapper


def test_func():
    """Тестовая функция."""
    print('        вызов тестовой функции')


# >>> test_func
# <function test_func at 0x000001812877F920>

# >>> test_func.__doc__
# 'Тестовая функция.'

# >>> test_func()
#         вызов тестовой функции

# >>> test_func = decorator(test_func)
# вызов decorator()
#   func_obj = <function test_func at 0x0000023D7025F9C0>
#   перед созданием функции-обёртки
#   после создания функции-обёртки

# >>> test_func
# <function decorator.<locals>.wrapper at 0x000001E3092CF9C0>

# >>> test_func.__doc__
# 'Функция-обёртка.'

# >>> test_func()
#     вызов wrapper()
#       перед вызовом декорируемой функции
#         вызов тестовой функции
#       после вызова декорируемой функции


@decorator
def adder(num1: int, num2: int) -> int:
    return num1 + num2

# инструкция @decorator является "синтаксическим сахаром" — другим способом записать следующее действие:
# adder = decorator(adder)

# вызов decorator()
#   func_obj = <function adder at 0x0000023D7025FB00>
#   перед созданием функции-обёртки
#   после создания функции-обёртки
# >>> adder
# <function decorator.<locals>.wrapper at 0x000001F8D8C8FA60>
# >>>
# >>> adder(5, 15)
    # вызов wrapper()
      # перед вызовом декорируемой функции
      # после вызова декорируемой функции
# 20
