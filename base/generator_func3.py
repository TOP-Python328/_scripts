def divergent_sequence(start: int, end: int) -> 'generator':
    while start < end:
        yield start
        yield -start
        start += 1


# >>> print(*divergent_sequence(1, 10))
# 1 -1 2 -2 3 -3 4 -4 5 -5 6 -6 7 -7 8 -8 9 -9

