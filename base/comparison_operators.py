# >>> 1 == 1
# True
# >>> 1 == 1.0
# True
# >>> (1 + 5) / 3 == [1, 2, 3][1]
# True

# >>> 1 != 1
# False

# >>> 2 > 1
# True
# >>> 2 > 2
# False

# >>> 2 >= 2
# True
# >>> 2 >= 3
# False

# >>> 2 < 3
# True
# >>> 2 <= 2
# True


prompt = ' введите число: '
n, m = int(input(prompt)), int(input(prompt))

n_greater_than_m = n > m

print('n > m:', n_greater_than_m)

#  введите число: 15
#  введите число: 20
# n > m: False
# >>>
# >>> type(n_greater_than_m)
# <class 'bool'>


# >>> 'a' == 'A'
# False
# >>>
# >>> 'aa' > 'ab'
# False
# >>>
# >>> ord('a')
# 97
# >>> ord('A')
# 65
# >>>
# >>> ord('b')
# 98
# >>>
# >>> 'd' > 'aaa'
# True
# >>>
# >>> '2' > '11'
# True
# >>> int('2') > int('11')
# False
# >>>
# >>> ord(' ')
# 32
# >>>
# >>> 'aa' == 'aaa'
# False
# >>>
# >>> 'di' > 'aaa'
# True