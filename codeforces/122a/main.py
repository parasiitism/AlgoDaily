
def f():
    s = input()
    hashset = set()
    for c in s:
        hashset.add(c)
    if sorted(list(hashset)) == ['4', '7']:
        return 'YES'
    x = int(s)
    if x % 4 == 0 or x % 7 == 0 or x % 47 == 0 or x % 74 == 0 or x % 477 == 0 or x % 774 == 0:
        return 'YES'
    return 'NO'


print(f())
