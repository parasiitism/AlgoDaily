"""
    navie brute force

    Time    O(n^2)
"""


def solution(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) % 2 == 0:
                count += 1
    return count


a = [1, 2, 3, 4, 5, 6]
print(solution(a))

"""
    better approach: math
    - odd + odd = even
    - even + even = even
    - so count the number of odds and evens
    - the number of combinations of pairs is n(n-1)/2

    e.g. [1,3,5,7]

    1,3
    1,5
    1,7
    3,5
    3,7
    5,7

    no of pairs = 4*(4-1)/2 = 6

    Time    O(n)
"""


def solution(nums):
    oddCount = 0
    evenCount = 0
    for num in nums:
        if num % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
    a = 0
    if oddCount > 1:
        a = oddCount*(oddCount-1)/2
    b = 0
    if evenCount > 1:
        b = evenCount*(evenCount-1)/2
    return a+b


a = [1, 2, 3, 4, 5, 6]
print(solution(a))
