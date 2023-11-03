class NonNaturalNumberError(Exception):
    pass


class Natural(int):
    def __new__(cls, value: int):
        instance = super().__new__(cls, value)
        if instance <= 0:
            raise NonNaturalNumberError
        return instance


# >>> Natural(5)
# 5
# >>>
# >>> Natural(-10)
# ...
# NonNaturalNumberError
# >>> 
# >>> Natural([1,2,3])
# ...
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
# >>>
# >>> Natural('abc')
# ...
# ValueError: invalid literal for int() with base 10: 'abc'


buffer = '12 ab (2,3) 0 -3 15'
natural_numbers = []
for obj in buffer.split():
    try:
        natural_numbers.append(Natural(obj))
    
    except NonNaturalNumberError as exc:
        # breakpoint()
        natural_numbers.append(1)
    
    except (TypeError, ValueError):
        pass

# >>> natural_numbers
# [12, 1, 1, 15]

