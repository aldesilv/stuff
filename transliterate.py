def transliterate(a):
    a = a.lower()
    if a == "kill yourself":
        return "love yourself"
    elif a == "you're dead":
        return "you're healthy"
    elif len(a) >= 8 and a[3:8] == "hates":
        return "he loves" + a [8:]
    elif a == "kill yourself":
        return "love yourself"
    elif a == "why don't you just suicide":
        return "why  don't you just live"
    return ""

if __name__ == "__main__":
    while True:
       a = input()
       print(f'{a} is {transliterate(a)}')
