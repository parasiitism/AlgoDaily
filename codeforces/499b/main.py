def f():
    n, m = map(int, input().split())

    map1 = {}
    map2 = {}
    for _ in range(m):
        first, second = input().split()
        map1[first] = second
        map2[second] = first

    sentence = input()
    words = sentence.split()
    res = []
    for w in words:

        first, second = None, None

        if w in map1:
            first = w
            second = map1[w]
        elif w in map2:
            first = map2[w]
            second = w

        if first != None and second != None:
            if len(first) < len(second):
                res.append(first)
            elif len(second) < len(first):
                res.append(second)
            elif len(first) == len(second):
                res.append(first)
        else:
            res.append(w)
    print(" ".join(res))


f()
