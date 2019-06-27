import heapq

"""
    Question: Lily's problem
    Lily has to solve a number of problems, 
    each of them when solved correctly give her a certain happiness value. 
    Each problem has a different happiness value. 
    Lily has to solve the first problem but after that for every problem(i) 
    she can either solve the next problem(i+1) or skip 1 problem to solve the (i+2)th problem. 
    She has to keep on solving until the maximum-minimum happiness value of the problems solved 
    is greater than/equal to an integer k. 
    What are the minimum number of problems she has to solve in order to achieve this?

    intutition: shortest path >= k
    
"""


def maxSumForNonAdjacent(nums, target):

    if target <= 0 or len(nums) == 0:
        return 0

    # total happiness, index, steps
    # use maxheap, so use a negative value
    q = [(-nums[0], 0, 1)]
    seen = set()
    while len(q) > 0:
        w, i, steps = q.pop(0)
        if -w >= target:
            return -w, steps
        # avoid redundant calculation
        if (w, i, steps) in seen:
            continue
        seen.add((w, i, steps))
        # explore options
        if i + 1 < len(nums):
            q.append((w - nums[i+1], i+1, steps+1))
        if i + 2 < len(nums):
            q.append((w - nums[i+2], i+2, steps+1))
    return 0


# [4, 4, 1] => 8
print(maxSumForNonAdjacent([4, 1, 1, 4, 2, 1], 8))

# [5, 10] => 15
print(maxSumForNonAdjacent([5, 5, 10, 100, 10, 5], 11))
