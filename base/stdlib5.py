from re import compile


pattern_binary = compile(r'(?:b|0b)?[01]+')


def is_binary(bin_number: str) -> bool:
    """"""
    return bool(pattern_binary.fullmatch(bin_number))


# >>> is_binary('0101')
# True
# >>> is_binary('b11')
# True
# >>> is_binary('0b11001')
# True
# >>> is_binary('1b0101')
# False
# >>> is_binary('10b101')
# False
# >>> is_binary('00b110')
# False
# >>> is_binary('00410')
# False

