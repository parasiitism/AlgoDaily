"""
    1st approach: back&forth

    e.g. [4, 3, 4, 4, 4, 2]
    forward  = [4, #, 4, 4, 4, 4]
    backward = [4, 4, 4, 4, #, 2]

    when forward[i-1] == backward[i], it means that the leader on the left == leader on the right

    so resutl = 2, because 
    forward[0] = backward[1]
    forward[2] = backward[3]

    Time    O(n)
    Space   O(2n)
    Result  100/100 https://app.codility.com/demo/results/trainingESG4KV-5SZ/
"""


def solution(nums):
    # go forward and record the freqNum at every index
    m = {}
    forward = len(nums) * [None]
    freqNum = None
    for i in range(len(nums)):
        num = nums[i]
        # count
        if num not in m:
            m[num] = 1
        else:
            m[num] += 1
        # compare
        if m[num] > (i+1)//2:
            freqNum = num
        # assign
        if freqNum in m and m[freqNum] > (i+1)//2:
            forward[i] = freqNum
        else:
            freqNum = None
    # go backward and record the freqNum at every index
    m = {}
    backward = len(nums) * [None]
    freqNum = None
    for i in range(len(nums)-1, -1, -1):
        num = nums[i]
        # count
        if num not in m:
            m[num] = 1
        else:
            m[num] += 1
        # compare
        if m[num] > (len(nums) - i)//2:
            freqNum = num
        # assign
        if freqNum in m and m[freqNum] > (len(nums) - i)//2:
            backward[i] = freqNum
        else:
            freqNum = None
    # when forward[i-1] == backward[i], it means that the leader on the left == leader on the right
    res = 0
    for i in range(1, len(nums)):
        if forward[i-1] == backward[i] and forward[i-1] != None:
            res += 1
    return res


a = [4, 3, 4, 4, 4, 2]
print(solution(a))

print("-----")

a = [4, 3, 4, 4, 2, 1, 0]
print(solution(a))

print("-----")

a = [4, 3, 4, 4, 4]
print(solution(a))

print('-----')

a = [1, 2, 3, 4, 5]
print(solution(a))
