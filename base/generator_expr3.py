words = ['кот', 'пёс', 'черепаха', 'лис', 'варан', 'ворон']

print(f'самое короткое слово: {min(len(word) for word in words)} буквы')
print(f'самое длинное слово: {max(len(word) for word in words)} буквы\n')

abbrev = ''.join(word[0].upper() for word in words)
print(repr(abbrev))

# >>> ' и '.join(words)
# 'кот и пёс и черепаха и лис и варан и ворон'

words_with_conjugate = ''
words_len = len(words)
for i, word in enumerate(words):
    words_with_conjugate += word + (' и ' if i != words_len-1 else '')

print(words_with_conjugate)

