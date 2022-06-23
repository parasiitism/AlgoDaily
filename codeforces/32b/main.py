def f():
    s = input()
    i = 0
    res = ''
    while i < len(s):
        if s[i] == '-':
            if s[i+1] == '-':
                res += '2'
            else:
                res += '1'
            i += 2
        else:
            res += '0'
            i += 1
    return res


print(f())
