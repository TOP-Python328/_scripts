def product(*numbers: int | float) -> int | float:
    # print(f'{type(numbers)}\n{numbers}')
    if 0 in numbers:
        return 0
    
    result = 1
    for num in numbers:
        result *= num
    return result


# тесты параметра numbers:

# >>> product(1, 2)
# <class 'tuple'>
# (1, 2)
# >>> 
# >>> product()
# <class 'tuple'>
# ()
# >>> 
# >>> product(*range(10, 60, 10))
# <class 'tuple'>
# (10, 20, 30, 40, 50)
# >>> 
# >>> product(a=123)
# ...
# TypeError: product() got an unexpected keyword argument 'a'

