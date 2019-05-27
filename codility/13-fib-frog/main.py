"""
    1st approach: dp + bfs + hashtable
    - use dp to get the Fibonacci sequence up to N
    - bfs to find the shortest path
    - use a hashtable to avoid redundant calculation 

    Time    O(nlogn)
    Space   O(n)

    Result: 100/100 https://app.codility.com/demo/results/trainingKBRXBC-UG9/
"""


def getFibUpTo(n):
    dp = [0, 1]
    i = 2
    while True:
        temp = dp[i-1] + dp[i-2]
        if temp > n:
            break
        dp.append(temp)
        i += 1
    # remove the first 2 because fibinacci starts with [0,1,1,2,3,5,8....]
    x = dp[2:]
    return x[::-1]


# print(getFibUpTo(100))
# print(getFibUpTo(5000))
print(getFibUpTo(100000))


def Solution(A):
    # add 1 at the end, such that we can use it when BFS
    A.append(1)
    # get fibinacci numbers up to N
    fibs = getFibUpTo(len(A))
    end = len(A)-1
    # in bfs, the first one who arrives the end must be the path with shortest depth
    seen = set()
    q = [(-1, 0)]
    while len(q) > 0:
        loc, steps = q.pop(0)
        # look for the options to move next
        for fib in fibs:
            nextLoc = loc + fib
            if nextLoc > end:
                continue
            elif nextLoc == end:
                # yeah
                return steps + 1
            elif nextLoc < len(A) and A[nextLoc] == 1:
                # avoid redundant calculation
                if nextLoc in seen:
                    continue
                seen.add(nextLoc)
                q.append((nextLoc, steps+1))
    return -1


A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
print(Solution(A))

A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(Solution(A))

A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(Solution(A))

A = 100000 * [0]
print(Solution(A))

A = 100000 * [1]
print(Solution(A))
