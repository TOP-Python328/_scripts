def infinite_counter(start: int, step: int = 1) -> 'generator':
    while True:
        yield start
        start += step


# >>> print(*zip(
# ...     infinite_counter(1),
# ...     ['hello', 'python', 'cool', 'lang']
# ... ))
# (1, 'hello') (2, 'python') (3, 'cool') (4, 'lang')

