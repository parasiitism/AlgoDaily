"""
    1st: BFS
    TLE
"""


class Approach1:

    def f():
        n = int(input())
        for _ in range(n):
            x = int(input())
            print(bfs(x))

    def bfs(n):
        q = [(n, 0)]
        seen = set()
        while len(q) > 0:
            x, steps = q.pop(0)
            if x == 1:
                return steps
            if x in seen:
                continue
            seen.add(x)
            if x * 2 <= 2*(10**9):
                q.append((x*2, steps+1))
            if x % 6 == 0:
                q.append((x//6, steps+1))
        return -1


# A1 = Approach1()
# A1.f()

"""
    2nd: math
    - When we divide by 6, it means divide by 2 and also divide by 3.
    - At the same time, multiply by 2 is also an operation
    - *** So if we have some 3s remaining to divide, 
        it means need to multiply by 2 such that we can divide by 6

    Time    O(logN)
    Space   O(1)
"""


class Approach2:

    def f(self):
        n = int(input())
        for _ in range(n):
            x = int(input())
            cnt2, cnt3 = 0, 0
            # remove all 2s
            while x % 2 == 0:
                x /= 2
                cnt2 += 1
            # remove all 3s
            while x % 3 == 0:
                x /= 3
                cnt3 += 1
            if x == 1 and cnt2 <= cnt3:
                print(2 * cnt3 - cnt2)
            else:
                print(-1)


A2 = Approach2()
A2.f()
