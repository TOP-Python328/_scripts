from random import randrange as rr, choice, sample
from string import ascii_lowercase as letters


words = []
flags = (True, False)
for _ in range(10):
    word = ''.join(sample(letters, k=rr(4, 10)))
    word = word.capitalize() if choice(flags) else word
    words.append(word)

print(*words, sep='\n')
