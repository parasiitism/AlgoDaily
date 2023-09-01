"""
    1st: Given a string and shift, encrypt the string by shifting the character.
    The rule is: whenever u see an integer, increment the shift value

    e.g.
    Input:
        AB2AB3AB, 3
    result:
        de2fg3ij
        ** ** ** 
        33 55 88 <- the shift value changes according to the integer we see in the message
"""
def f1(msg, shift):
    pfs = shift
    res = ''
    for c in msg:
        if c.isdigit():
            pfs += int(c)
            res += c
        elif c.isalpha():
            base = ord('a')
            idx = (ord(c) - ord('a') + pfs) % 26
            res += chr(base + idx)
        else:
            res += c
    return res

print(f1('he2l9lo wo1rld@', 3))
print(f1('ab2ab3ab', 3))

"""
    2nd:
    - support any size of integers and decrement
"""
def f2(msg, shift):
    sign = 1
    pfs = shift
    num = 0
    res = ''
    for c in msg:
        if c.isdigit():
            num = num * 10 + int(c)
            res += c
        elif c == '-':
            sign = -1
            res += c
        elif c.isalpha():
            base = ord('a')
            if sign == 1:
                pfs += num
            else:
                pfs -= num
                sign = 1
            num = 0
            idx = (ord(c) - ord('a') + pfs) % 26
            res += chr(base + idx)
        else:
            res += c
    return res

print(f2('he12l9lo wo-1rld', 7))

"""
    3rd
    - support reverse mode by using a character '!'
    e.g.
    - !a, 1 => y
    - !b, 1 => x

"""
def f3(msg, shift):
    sign = 1
    pfs = shift
    num = 0
    res = ''
    should_reverse = False
    for c in msg:
        if c.isdigit():
            num = num * 10 + int(c)
            res += c
        elif c == '-':
            sign = -1
            res += c
        elif c == '!':
            should_reverse = not should_reverse
            res += c
        elif c.isalpha():
            base = ord('a')
            if sign == 1:
                pfs += num
            else:
                pfs -= num
                sign = 1
            num = 0
            idx = (ord(c) - ord('a') + pfs) % 26
            if should_reverse:
                idx = (25 - idx) % 26
            res += chr(base + idx)
        else:
            res += c
    return res

print(f3('he12!l9lo wo!-1rld', 12))
print(f3('!l', 16))

"""
    4th:
    - adding a scope presented by ( and )
    
"""
def f4(msg, shift):
    chars = [c for c in msg]
    return recur(chars, shift)

def recur(chars, shift, _sign=1, _should_reverse=False):
    sign = _sign
    pfs = shift
    num = 0
    res = ''
    should_reverse = _should_reverse
    while len(chars) > 0:
        c = chars.pop(0)
        if c.isdigit():
            num = num * 10 + int(c)
            res += c
        elif c == '-':
            sign = -1
            res += c
        elif c == '!':
            should_reverse = not should_reverse
            res += c
        elif c == '(':
            res += c
            if sign == 1:
                pfs += num
            else:
                pfs -= num
                sign = 1
            num = 0
            res += recur(chars, pfs, sign, should_reverse)
        elif c == ')':
            res += c
            return res
        elif c.isalpha():
            base = ord('a')
            if sign == 1:
                pfs += num
            else:
                pfs -= num
                sign = 1
            num = 0
            idx = (ord(c) - ord('a') + pfs) % 26
            if should_reverse:
                idx = (25 - idx)%26
            res += chr(base + idx)
        else:
            res += c
    return res

print(f4('he12(!l(9lo w)o!-1r)ld', 30))