
def f():
    s = input()
    s = s.lower()
    res = ''
    for i in range(len(s)):
        if s[i] in 'aeiouy':
            continue
        res += '.' + s[i]
    return res


print(f())
