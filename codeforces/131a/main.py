
def f():
    S = input()
    if S == S.upper():
        return S.lower()
    isFirstSmall = False
    first = S[0]
    if 0 <= ord(first) - ord("a") < 26:
        isFirstSmall = True
    areTheRestCap = True
    for i in range(1, len(S)):
        c = S[i]
        j = ord(c) - ord("A")
        if j < 0 or j >= 26:
            areTheRestCap = False
            break
    if isFirstSmall and areTheRestCap:
        return S[0].upper() + S[1:].lower()
    return S


print(f())
