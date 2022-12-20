
def f():
    T = int(input())
    for _ in range(T):
        s = input()
        t = input()
        b = solve(s, t)
        if b:
            print("YES")
        else:
            print("NO")


def solve(s, t):
    seen = ''
    rev_seen = ''
    for i in range(len(s)):
        c = s[i]
        seen += c
        temp = seen + rev_seen
        if t in temp:
            return True
        rev_seen = c + rev_seen
    return False


# solve('abcdef', 'fedc')
f()
