text = 'ab cd ef gh'
text_len = len(text)
i = 0

while i <= text_len:
    try:
        text[i]
    except IndexError:
        break
    i += 1

