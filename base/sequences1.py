text = 'Python is cool!'

print(len(text), type(text), type(text[0]), sep='\n', end='\n\n')

hex_number = 'f0'

# numbers_str = '[1, 2, 3]'

# numbers = list(numbers_str)
# print(numbers)

# numbers = [int(n) for n in numbers_str.strip('[]').split(', ')]
# print(numbers)


print(
    f'index = 0: {text[0]}', 
    f'index = 1: {text[1]}', 
    f'index = 2: {text[2]}', 
    f'index = 14: {text[14]}', 
    sep='\n',
    end='\n\n'
)

var = text[0] == text[2]
print(var)


file1_name = 'Классификация коллекций.docx'
file2_name = 'Методы последовательностей.pdf'

file1_name_len = len(file1_name)
file1_name[file1_name_len - 1]

print(
    f'index = -4: {file1_name[-4]}', 
    f'index = -3: {file1_name[-3]}', 
    f'index = -2: {file1_name[-2]}', 
    f'index = -1: {file1_name[-1]}', 
    f'index = -3: {file2_name[-3]}', 
    f'index = -2: {file2_name[-2]}', 
    f'index = -1: {file2_name[-1]}', 
    sep='\n',
    end='\n\n'
)

print(
    'НД'[True],
    'НД'[False],
    sep='\n',
    end='\n\n'
)


# >>> b = 'abc'
# >>> id(b)
# 140724583861824

# >>> b += 'def'
# >>> b
# 'abcdef'
# >>> id(b)
# 2171834796208

# >>> b = b + 'ghi'
# >>> b
# 'abcdefghi'
# >>> id(b)
# 2171834796016

# >>> b *= 2
# >>> b
# 'abcdefghiabcdefghi'
# >>> id(b)
# 2171834629968
