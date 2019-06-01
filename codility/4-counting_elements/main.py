"""
    1st approach: hashtable

    Time    O(n)
    Space   O(n)
    result 100/100 https://app.codility.com/demo/results/trainingT8S544-9YR/
"""


def solution(A):
    # write your code in Python 3.6
    hs = set()
    for num in A:
        if num in hs:
            return 0
        else:
            hs.add(num)
    i = 1
    while i in hs:
        i += 1
    if i == len(A) + 1:
        return 1
    return 0


print(solution([4, 3, 2, 5, 1]))
print(solution([4, 3, 2, 5]))
