
"""
    Time    O(N)
    Space   O(N)
"""


def f():
    n, t = [int(s) for s in input().split(" ")]
    s = input()
    temp = [c for c in s]
    seen = set()
    for i in range(t):
        key = tuple(temp)
        if key in seen:
            break
        seen.add(key)
        _temp = []
        j = 0
        while j < n:
            if temp[j] == 'G':
                _temp.append('G')
                j += 1
            elif j+1 < n and temp[j+1] == 'G':
                _temp.append('G')
                _temp.append('B')
                j += 2
            else:
                _temp.append('B')
                j += 1
        temp = _temp
    return ''.join(temp)


print(f())
