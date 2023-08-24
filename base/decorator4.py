def excepter(exception_cls):
    def decorator(func_obj):
        def wrapper(*args, **kwargs):
            try:
                res = func_obj(*args, **kwargs)
            except exception_cls:
                print('перехват нужного исключения')
            else:
                return res
        return wrapper
    return decorator


@excepter(ZeroDivisionError)
def divider(num1, num2):
    return num1 / num2


# >>> divider(2, 4)
# 0.5
# >>> divider(2, 0)
# перехват нужного исключения

