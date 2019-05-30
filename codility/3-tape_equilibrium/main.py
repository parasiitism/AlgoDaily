import sys

"""
    1st approach: prefix sum from both sides

    Time    O(3n) -> O(n^2)
    Space   O(n)
    Result 69/100 https://app.codility.com/demo/results/trainingKHYEU3-VEZ/
"""


def solution(A):
    # write your code in Python 3.6
    sumFromFront = []
    prevSum = 0
    for i in range(len(A)):
        prevSum += A[i]
        sumFromFront.append(prevSum)

    sumFromEnd = []
    prevSum = 0
    for i in range(len(A)-1, -1, -1):
        prevSum += A[i]
        sumFromEnd.insert(0, prevSum)  # it takes O(k) so 69/100

    res = sys.maxsize
    for i in range(1, len(A)):
        temp = abs(sumFromFront[i-1] - sumFromEnd[i])
        res = min(res, temp)
    return res


print(solution([3, 1, 2, 4, 3]))

print("-----")


"""
    1st approach: prefix sum from both sides

    Time    O(3n)
    Space   O(n)
    Result 69/100 https://app.codility.com/demo/results/trainingGRYC6M-NM9/
"""


def solution(A):
    # write your code in Python 3.6
    sumFromFront = []
    prevSum = 0
    for i in range(len(A)):
        prevSum += A[i]
        sumFromFront.append(prevSum)

    sumFromEnd = []
    prevSum = 0
    for i in range(len(A)-1, -1, -1):
        prevSum += A[i]
        sumFromEnd.append(prevSum)
    sumFromEnd = sumFromEnd[::-1]

    res = sys.maxsize
    for i in range(1, len(A)):
        temp = abs(sumFromFront[i-1] - sumFromEnd[i])
        res = min(res, temp)
    return res


print(solution([3, 1, 2, 4, 3]))
