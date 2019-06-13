import string

def is_pangram(s):
    alphabets = list(map(chr, range(97, 123)))
    l1 = s.lower()
    l2 = []
    for a in l1:
        if a in alphabets and a not in l2:
            l2.append(a)
    if len(l2) == 26:
        return True
    return False


pangram = "Cwm fjord bank glyphs vext quiz"
print(is_pangram(pangram))