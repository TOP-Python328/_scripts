def calculator(
        # параметры до / — строго позиционные
        num1: int, 
        num2: int, 
        /, 
        *, 
        # параметр после * — строго ключевой
        operation: str
) -> int | float:
    ...


# >>> calculator(1, 2, operation='-')


def process_point(x: int, y: int, /):
    ...


# process_point(1, 1)
# process_point(y=-2, x=1)
# process_point(x=-2, y=1)

process_point(1, 1)
process_point(1, -2)
process_point(-2, 1)

