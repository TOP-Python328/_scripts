numbers = [9, -2, 3, 0, 1, 13, 15, 8, -4]

# >>> print(*sorted(numbers))
# -4 -2 0 1 3 8 9 13 15

# >>> print(*sorted(numbers, key=lambda n: abs(n)))
# 0 1 -2 3 -4 8 9 13 15

# >>> print(*sorted(numbers, key=lambda n: n > avg))
# -2 3 0 1 -4 9 13 15 8

words = ['hello', 'python', '9', 'cool', 'language', '14']

# >>> print(*sorted(words))
# 14 9 cool hello language python

# >>> print(*sorted(words, key=lambda w: len(w)))
# 9 14 cool hello python language

# >>> print(*sorted(words, key=lambda w: digits & set(w)))
# hello python cool language 9 14
