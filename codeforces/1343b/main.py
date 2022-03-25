"""
    2 4 = 6
    1 5 = 6

    2 4 6 = 12
    1 3 x

    2 4 6 8 = 20
    1 3 5 11 = 20

    2 4 6 8 10 = 30
    1 3 5 7 x

    2 4 6 8 10 12 = 42
    1 3 5 7 9  17 = 42
"""


def f():
    T = int(input())
    for _ in range(T):
        n = int(input())
        half = n//2
        if half % 2 == 1:
            print("NO")
        else:
            print("YES")
            evens = []
            evens_sum = 0
            odds = []
            odds_sum = 0
            for i in range(1, half+1):
                evens.append(2*i)
                evens_sum += 2*i
                if i+1 < half+1:
                    odds.append(2*i-1)
                    odds_sum += 2*i-1
            odds.append(evens_sum - odds_sum)
            for x in evens + odds:
                print(x, end=" ")


f()
