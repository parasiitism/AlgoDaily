import math

"""
              / summation of (x - avg)^2 \
    sd = sqrt(----------------------------)
              \             n            /
"""


def solution(nums):
    avgN = 0
    for num in nums:
        avgN += num
    avg = avgN/(len(nums)*1.0)
    summation = 0
    for num in nums:
        summation += (num - avg)**2
    return math.sqrt(summation/(len(nums)*1.0))


a = [4, 9, 11, 12, 17, 5, 8, 12, 14]
print(solution(a))
