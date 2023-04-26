"""
    Given an array of numbers, determine if every item is a sum of 2 fibonacci numbers
    - the range of A[i]: 1 <= A[i] <= 10**18, there are only 87 fibonacci numbers within the range
    - then we can just use 2 pointers

    Time    O(AN)
    Space   O(A+N)
"""


def f(A):
    fibs = get_fib()
    res = []
    for x in A:
        found = False
        left = 0
        right = len(fibs) - 1
        while left <= right:
            total = fibs[left] + fibs[right]
            if total < x:
                left += 1
            elif total > x:
                right -= 1
            else:
                found = True
                break
        res.append(found)
    return res


def get_fib():
    dp = [1, 1]
    while dp[-1] < 10**18:
        dp.append(dp[-1] + dp[-2])
    return dp


print(f([2, 5, 17, 267914299, 267914298]))
