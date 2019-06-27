import sys
"""
    Integer V lies strictly between integers U and W if U < V < W or if U > V > W.
    A non-empty zero-indexed array A consisting of N integers is given. 
    A pair of indices (P, Q), where 0 <= P < Q < N, is said to have adjacent values if no value 
    in the array lies strictly between values A[P] and A[Q]
    
    For example, in array A such that: [0, 3, 3, 7, 5, 3, 11, 1]

    the following pairs of indices have adjacent values:
    (0, 7), (1, 2), (1, 4),
    (1, 5), (1, 7), (2, 4),
    (2, 5), (2, 7), (3, 4),
    (3, 6), (4, 5), (5, 7)

    For example, indices 4 and 5 have adjacent values because there is no value in array A that lies 
    strictly between A[4] = 5 and A[5] = 3; the only such value could be the number 4, 
    and it is not present in the array.
    
    Write a function that returns the maximum distance between indices that have adjacent values
"""

"""
    1st approach:
    - sort the array and record the index
    - iterate the sorted array and get the max-diff between indices

    Time    O(nlogn)
    Space   O(n)
"""


class Solution(object):
    def maxdiff(self, nums):
        arr = []
        for i in range(len(nums)):
            arr.append((nums[i], i))
        arr = sorted(arr, key=lambda x: x[0])
        print(arr)
        maxDiff = 0
        for i in range(1, len(arr)):
            prev, prevIdx = arr[i-1]
            cur, curIdx = arr[i]
            diff = abs(curIdx-prevIdx)
            maxDiff = max(maxDiff, diff)
        return maxDiff


a = [0, 3, 3, 7, 5, 3, 11, 1]
print(Solution().maxdiff(a))

a = [6, 0, 5, 7, 1, 8]
print(Solution().maxdiff(a))

print("-----")

"""
    Variation: number of adjacent pairs

    Integer V lies strictly between integers U and W if U < V < W or if U > V > W.
    A non-empty zero-indexed array A consisting of N integers is given. 
    A pair of indices (P, Q), where 0 <= P < Q < N, is said to have adjacent values if no value 
    in the array lies strictly between values A[P] and A[Q]
    
    For example, in array A such that: [0, 3, 3, 7, 5, 3, 11, 1]

    the following pairs of indices have adjacent values:
    (0, 7), (1, 2), (1, 4),
    (1, 5), (1, 7), (2, 4),
    (2, 5), (2, 7), (3, 4),
    (3, 6), (4, 5), (5, 7)

    For example, indices 4 and 5 have adjacent values because there is no value in array A that lies 
    strictly between A[4] = 5 and A[5] = 3; the only such value could be the number 4, 
    and it is not present in the array.
    
    Write a function that returns number of adjacent values
"""


class Solution(object):
    def countdjacentPairs(self, nums):
        arr = sorted(nums)
        prev = sys.maxsize
        prevCount = 0
        cur = arr[0]
        curCount = 1
        result = 0
        for i in range(1, len(arr)):
            if arr[i] == cur:
                curCount += 1
                result += curCount - 1
                result += prevCount
            else:
                result += curCount
                prev = cur
                prevCount = curCount
                cur = arr[i]
                curCount = 1
        return result


a = [0, 3, 3, 7, 5, 3, 11, 1]
print(Solution().countdjacentPairs(a))
