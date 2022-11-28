"""
    Array
    - remove the adjacent neightbours at the same level
    - mind the wording "exactly one" in the description

    Time    O(N)
    Space   O(N) worst for the distincts
"""


def f():
    T = int(input())
    for _ in range(T):
        _ = input()
        nums = [int(c) for c in input().split()]
        b = solve(nums)
        print('YES' if b else 'NO')


def solve(nums):
    n = len(nums)
    distincts = []
    for i in range(n):
        if i == 0 or nums[i] != distincts[-1]:
            distincts.append(nums[i])
    valley_cnt = 0
    N = len(distincts)
    for i in range(N):
        if (i == 0 or distincts[i-1] > distincts[i]) and (i == N-1 or distincts[i] < distincts[i+1]):
            valley_cnt += 1
    return valley_cnt == 1


# print(solve([3, 2, 2, 1, 2, 2, 3]))
# print(solve([1, 1, 1, 2, 3, 3, 4, 5, 6, 6, 6]))
# print(solve([1, 2, 3, 4, 3, 2, 1]))
# print(solve([9, 7, 4, 6, 9, 9, 10]))
# print(solve([2, 2]))
# print(solve([9, 4, 4, 5, 9, 4, 9, 10]))
# print(solve([9, 0, 0, 5, 3, 5, 0, 0, 9]))
# print(solve([2, 7, 5, 8, 8, 4, 10, 2]))
# print(solve([10, 10, 8, 10, 10, 4]))
# print(solve([5, 6, 6, 4, 4, 5]))

f()
