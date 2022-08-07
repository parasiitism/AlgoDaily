# from collections import *
"""
    1st: DFS + caching
    
    Time    O(N)
    Space   O(N)
    MLE
"""
# def f():
#     n = int(input())
#     nums = [0]
#     for i in range(n):
#         x = int(input())
#         nums.append(x)
#     res = 1
#     seen = defaultdict(int)

#     def dfs(node):
#         if node == -1:
#             return 0
#         if node in seen:
#             return seen[node]
#         parent = nums[node]
#         depth = dfs(parent) + 1
#         seen[node] = depth
#         return depth

#     for idx in range(1, n+1):
#         res = max(res, dfs(idx))

#     print(res)

"""
    2nd: just simply find the root
    - in practice, having no recursion and hashtable spends a fewer resources

    Time    O(N)
    Space   O(N)
    MLE
"""


def f():
    n = int(input())
    nums = [0]
    for i in range(n):
        x = int(input())
        nums.append(x)
    res = 0
    for i in range(1, n+1):
        cur = nums[i]
        count = 1
        while cur != -1:
            count += 1
            cur = nums[cur]
        res = max(res, count)
    print(res)


f()
