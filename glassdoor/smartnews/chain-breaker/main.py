import sys

"""
    Given a zero-indexed array A of N integers, returns the minimal cost of dividing chain into three pieces at 2 non-adjacent positions.
    More precisely, we should break links P, Q (0 < P < Q < N - 1, Q - P > 1) The total cost of this operation is equal to A[P] + A[Q].
    
    A = [5,2,4,6,3,7]
    
    We can choose to break the following links:
    (1, 3): total cost is 2 + 6 = 8 
    (1, 4): total cost is 2 + 3 = 5 
    (2, 4): total cost is 4 + 3 = 7 
    
    Write a function:
    class Solution { public int solution(int[] A); }
    that, given a zero-indexed array A of N integers, returns the minimal cost of dividing chain into three pieces.
    For example, given:
    A[0] = 5
    A[1] = 2
    A[2] = 4
    A[3] = 6
    A[4] = 3
    A[5] = 7
    the function should return 5, as explained above.

    ref:
    - https://github.com/htoma/codility/blob/master/codility/Code/ChainBreaker.cs
    - https://www.1point3acres.com/bbs/interview/machine-learning-485949.html

    A = [3, 2, 1, 4, 3 ,5, -2, -1, 10, 9]
               ^            ^
"""


def f(nums):
    """
        1st approach: sort + compare
        - sort
        - compare, the result must be from the 3 smallest items

        e.g. [....-3,-4,-3,.....]

        -3-4 = -7 but they are adajent
        -4-3 = -7 but they are adajent
        -3-3 = -6 they are non-adajent finally

        Time    O(nlogn)
    """
    arr = []
    for i in range(1, len(nums)-1):
        arr.append([nums[i], i])
    arr = sorted(arr, key=lambda x: x[0])
    a = arr[0]
    b = arr[1]
    c = arr[2]
    if abs(a[1] - b[1]) > 1:
        return a[0] + b[0], a[1], b[1]
    elif abs(a[1] - c[1]) > 1:
        return a[0] + c[0], a[1], c[1]
    elif abs(b[1] - c[1]) > 1:
        return b[0] + c[0], b[1], c[1]


a = [3, 2, 1, 4, 3, 5, -2, -1, 10, 9]
print(f(a))

a = [3, 2, -2, -4, -3, 5, -2, -1, 10, 9]
print(f(a))

a = [3, 2, -3, -4, -3, -2, -1, 0, 10, 9]
print(f(a))

a = [3, 2, -3, -3, -3, -3, -1, 0, 10, 9]
print(f(a))

a = [5, 2, 4, 6, 3, 7]
print(f(a))

print("-----")


def f(nums):
    """
        1st approach: get the 3 min values + compare
        - get the 3 min values in a loop
        - compare, the result must be from the 3 smallest items

        e.g. [....-3,-4,-3,.....]

        -3-4 = -7 but they are adajent
        -4-3 = -7 but they are adajent
        -3-3 = -6 they are non-adajent finally

        Time    O(n)
    """
    a = (sys.maxsize, -1)
    b = (sys.maxsize, -1)
    c = (sys.maxsize, -1)
    for i in range(1, len(nums)-1):
        num = nums[i]
        if num < a[0]:
            c = b
            b = a
            a = (num, i)
        elif num < b[0]:
            c = b
            b = (num, i)
        elif num < c[0]:
            c = (num, i)

    if abs(a[1] - b[1]) > 1:
        return a[0] + b[0], a[1], b[1]
    elif abs(a[1] - c[1]) > 1:
        return a[0] + c[0], a[1], c[1]
    elif abs(b[1] - c[1]) > 1:
        return b[0] + c[0], b[1], c[1]


a = [3, 2, 1, 4, 3, 5, -2, -1, 10, 9]
print(f(a))

a = [3, 2, -2, -4, -3, 5, -2, -1, 10, 9]
print(f(a))

a = [3, 2, -3, -4, -3, -2, -1, 0, 10, 9]
print(f(a))

a = [3, 2, -3, -3, -3, -3, -1, 0, 10, 9]
print(f(a))

a = [5, 2, 4, 6, 3, 7]
print(f(a))

print("-----")
