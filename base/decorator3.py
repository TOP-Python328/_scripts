def decorator_parametrizer(parameter) -> 'function':
    """Функция параметризации декораторов."""
    def decorator(func_obj: 'function') -> 'function':
        """Функция-декоратор."""
        def wrapper(*args, **kwargs):
            ...
            print(parameter)
            ...
            res = func_obj(*args, **kwargs)
            ...
            return res
        return wrapper
    return decorator


def test_func():
    print('вызов тестовой функции')


# >>> test_func = decorator_parametrizer('тестовый параметр')(test_func)
# >>> test_func()
# тестовый параметр
# вызов тестовой функции


@decorator_parametrizer('второй тестовый параметр')
def test_func2():
    print('вызов второй тестовой функции')


# >>> test_func2()
# второй тестовый параметр
# вызов второй тестовой функции
