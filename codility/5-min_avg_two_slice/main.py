import sys

"""
    1st approach: brute force

    Time    O(n^2)
    Space   O(1)
    Result 50/100
    https://app.codility.com/demo/results/training2Q8EC6-9CC/
"""


def solution(nums):
    cur = sys.maxsize
    res = 0
    for i in range(len(nums)):
        a = nums[i]
        for j in range(i+1, len(nums)):
            a += nums[j]
            avg = a / float(j-i+1)
            if avg < cur:
                # print("hi", avg)
                cur = avg
                res = i
    return res


a = [4, 2, 2, 5, 1, 5, 8]
print(solution(a))

a = [4, 2, 2, 5, -1, 5, -8]
print(solution(a))

a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(solution(a))

a = [8, 73, 2, 3, 45, 67, 89]
print(solution(a))


print("-----")


"""
    2nd approach: dp similar to lc53: max sum subarray

    Time    O(n)
    Space   O(1)
    Result 100/100
    https://app.codility.com/demo/results/trainingFCFK6V-6VJ/
"""


def solution(nums):
    res = 0
    minAvg = sys.maxsize
    curSum = nums[0]
    curIdxs = [0]
    for i in range(1, len(nums)):
        # extend
        avg1 = (curSum+nums[i])/float(len(curIdxs)+1)
        # now
        avg2 = (nums[i-1]+nums[i])/2.0
        # compare
        if avg1 <= avg2:
            curSum += nums[i]
            curIdxs.append(i)
            if avg1 < minAvg:
                minAvg = curSum/float(len(curIdxs))
                res = curIdxs[0]
        else:
            curSum = nums[i-1]+nums[i]
            curIdxs = [i-1, i]
            if avg2 < minAvg:
                minAvg = curSum/float(len(curIdxs))
                res = curIdxs[0]
    return res


a = [4, 2, 2, 5, 1, 5, 8]
print(solution(a))

a = [4, 2, 2, 5, -1, 5, -8]
print(solution(a))

a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(solution(a))

a = [8, 73, 2, 3, 45, 67, 89]
print(solution(a))
