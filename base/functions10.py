def print_return(*args, sep: str = ' ', end: str = '\n') -> str:
    return sep.join(str(arg) for arg in args) + end


def table_print(
        # позиционно-ключевой
        column1: list[str], 
        # позиционные
        *columns: list[str], 
        # строго ключевой
        v_sep: str = '|'
) -> str:
    # print(f'{column1=}, {columns=}')
    columns = column1, *columns
    widths = [
        max(len(str(elem)) for elem in col)
        for col in columns
    ]
    return '\n'.join(
        f'{v_sep} ' + f' {v_sep} '.join(
            f'{cell:^{widths[i]}}' 
            for i, cell in enumerate(row)
        ) + f' {v_sep}' 
        for row in zip(*columns)
    )
    

# тесты параметров column1 и columns:

# >>> table_print(*range(1, 5))
# column1=1, columns=(2, 3, 4)

# >>> table_print(*list('HELLO'))
# column1='H', columns=('E', 'L', 'L', 'O')

# >>> print(table_print([1, 100, -3], [20, 91, 3], [1000, -34, 0]))
# |  1  | 20 | 1000 |
# | 100 | 91 | -34  |
# | -3  | 3  |  0   |
