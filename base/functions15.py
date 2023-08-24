def process_text(word_processor: 'function', text: str) -> str:
    """"""
    return ' '.join(
        word_processor(word)
        for word in text.split()
    )


punctuation = '.,:;!?\'\"()*%-–—#[]{}'

def strip_punctuation(word: str) -> str:
    return word.strip(punctuation)


def caesar_encode(word: str, shift: int = 3) -> str:
    return ''.join(
        chr((ord(ch.lower()) - 97 + shift) % 26 + 97) if ch.isalpha() else ch
        for ch in word
    )


text = 'Return base to the power exp; if mod is present, return base to the power exp, modulo mod (computed more efficiently than pow(base, exp) % mod). The two-argument form pow(base, exp) is equivalent to using the power operator: base**exp.'

# >>> process_text(strip_punctuation, text)
# 'Return base to the power exp if mod is present return base to the power exp modulo mod computed more efficiently than pow(base exp  mod The two-argument form pow(base exp is equivalent to using the power operator base**exp'

# >>> process_text(caesar_encode, text)
# 'uhwxuq edvh wr wkh srzhu has; li prg lv suhvhqw, uhwxuq edvh wr wkh srzhu has, prgxor prg (frpsxwhg pruh hiilflhqwob wkdq srz(edvh, has) % prg). wkh wzr-dujxphqw irup srz(edvh, has) lv htxlydohqw wr xvlqj wkh srzhu rshudwru: edvh**has.'

