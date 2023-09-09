from functools import wraps
from time import perf_counter_ns as pc_ns


def elapse(func_obj: 'function') -> 'function':
    """"""
    @wraps(func_obj)
    def wrapper(*args, **kwargs):
        start = pc_ns()
        res = func_obj(*args, **kwargs)
        end = pc_ns()
        print(f'elapsed time for {func_obj.__name__}(): {end-start} ns')
        return res

    return wrapper


@elapse
def table_print(
        column1: list[str], 
        *columns: list[str], 
        v_sep: str = '|'
) -> str:
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

# >>> columns = [1, 100, -3], [20, 91, 3], [1000, -34, 0]
# >>>
# >>> print(table_print(*columns))
# elapsed time for table_print(): 53600 ns
# |  1  | 20 | 1000 |
# | 100 | 91 | -34  |
# | -3  | 3  |  0   |


@elapse
def product(*numbers: int | float) -> int | float:
    if 0 in numbers:
        return 0
    
    result = 1
    for num in numbers:
        result *= num
    return result


# >>> product(*range(1, 10))
# elapsed time for product(): 7900 ns
# 362880
# >>>
# >>> product(*range(10, 100))
# elapsed time for product(): 17300 ns
# 2571820310955251121078572499345973889184192247144555265338209983884964726444827921322240519625124511856638500904630284343341744128000000000000000000000
# >>>
# >>> product(*range(-50, 50))
# elapsed time for product(): 5600 ns
# 0

