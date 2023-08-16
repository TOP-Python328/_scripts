# функция принимает два обязательных аргумента
def adder(number1: int, number2: int) -> int:
    return number1 + number2


print(adder(1, 9), adder(20, -20), sep='\n', end='\n\n')

# >>> adder(5)
# ...
# TypeError: adder() missing 1 required positional argument: 'number2'

# >>> adder(5, 4, 6)
# ...
# TypeError: adder() takes 2 positional arguments but 3 were given


# функция принимает один обязательный аргумент и один необязательный аргумент
def split_text(text: str, separator: str = ' ') -> list[str]:
    return text.split(separator)


print(
    split_text('ab!cd!ef', '!'), 
    split_text('ab!cd ef!gh'), 
    sep='\n', 
    end='\n\n'
)

