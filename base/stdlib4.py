from math import factorial
from time import perf_counter as pc, perf_counter_ns as pc_ns


def factorial_user(number: int) -> int:
    result = number
    while number > 1:
        number -= 1
        result *= number
    return result


start = pc()
factorial_user(1000)
end = pc()
print(f'elapsed time for factorial_user(1000): {end-start:.5f} s')

start = pc_ns()
factorial(1000)
end = pc_ns()
print(f'elapsed time for factorial(1000): {end-start} ns')

