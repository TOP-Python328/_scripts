from itertools import chain, islice


numbers = range(10, 100, 10)
words = set('abcdef')

# >>> print(*chain(numbers, words), end='\n\n')
# 10 20 30 40 50 60 70 80 90 f a d e b c

squares = {
    'a1': 'black',
    'a2': 'white',
    'a3': 'black',
    'a4': 'white',
    'a5': 'black',
    'a6': 'white',
    'a7': 'black',
    'a8': 'white',
}

# >>> print(*islice(squares, 0, None, 2))
# a1 a3 a5 a7
