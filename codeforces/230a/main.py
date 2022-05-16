def f():
    s, n = map(int, input().split())
    duels = []
    for _ in range(n):
        strength, reward = map(int, input().split())
        duels.append([strength, reward])
    duels.sort(key=lambda x: (x[0], -x[1]))
    for strength, reward in duels:
        if s <= strength:
            return "NO"
        s += reward
    return "YES"


print(f())
