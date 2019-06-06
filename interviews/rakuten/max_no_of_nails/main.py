"""
    1st approach: hashtable counting
    - count the occurence(by storing the indeces) for each number
    - for each number, res = count + min(K, number of remaining items in array A)

    Time    O(n)
    Space   O(n)    hashtable
"""


def Solution(A, K):
    # if K is much larger, then we hammer down all the nails
    if K >= len(A):
        return len(A)
    # K must be >= 0
    if K < 0:
        K = 0
    N = len(A)
    # count the occurence(by storing the indeces) for each number
    ht = {}
    for i in range(N):
        num = A[i]
        if num not in ht:
            ht[num] = [i]
        else:
            ht[num].append(i)
    # for each number, res = count + min(K, number of remaining items in array A)
    best = 0
    for key in ht:
        indeces = ht[key]  # the length of indeces is the number of occurence
        temp = len(indeces) + min(K, N-indeces[-1]-1)
        best = max(best, temp)
    return best


a = [1, 1, 3, 3, 3, 4, 5, 5, 5, 5]
b = 2
print(Solution(a, b))

a = [1, 1, 3, 3, 3, 4, 5, 5, 5, 5]
b = 3
print(Solution(a, b))

a = [1, 1, 3, 3, 3, 4, 4, 5, 5, 5, 5]
b = 2
print(Solution(a, b))

a = [5, 5, 5, 5]
b = 2
print(Solution(a, b))

a = [1, 1, 3, 3, 3, 4, 5, 5, 5, 5]
b = 10
print(Solution(a, b))

a = [1, 1, 1, 2]
b = 2
print(Solution(a, b))

a = [1, 1, 1, 2]
b = 0
print(Solution(a, b))

a = [1, 2, 3, 4, 5]
b = 4
print(Solution(a, b))

a = [1, 2, 3, 4, 5]
b = 3
print(Solution(a, b))

print("-----")

"""
    2nd approach: counting
    - iterate through the array A to calculate the count on every height of nails
    - for each number, res = count + min(K, number of remaining items in array A)

    Time    O(n)
    Space   O(1)
"""


def Solution(A, K):
    # if K is much larger, then we hammer down all the nails
    if K >= len(A):
        return len(A)
    # K must be >= 0
    if K < 0:
        K = 0
    N = len(A)
    # count the occurence(by storing the indeces) for each number
    curHeight = -1
    curCount = 0
    best = 0
    for i in range(N):
        num = A[i]
        if num == curHeight:
            curCount += 1
        else:
            curHeight = num
            curCount = 1
        curBest = curCount + min(K, N-i-1)
        best = max(best, curBest)
    return best


a = [1, 1, 3, 3, 3, 4, 5, 5, 5, 5]
b = 2
print(Solution(a, b))

a = [1, 1, 3, 3, 3, 4, 5, 5, 5, 5]
b = 3
print(Solution(a, b))

a = [1, 1, 3, 3, 3, 4, 4, 5, 5, 5, 5]
b = 2
print(Solution(a, b))

a = [5, 5, 5, 5]
b = 2
print(Solution(a, b))

a = [1, 1, 3, 3, 3, 4, 5, 5, 5, 5]
b = 10
print(Solution(a, b))

a = [1, 1, 1, 2]
b = 2
print(Solution(a, b))

a = [1, 1, 1, 2]
b = 0
print(Solution(a, b))

a = [1, 2, 3, 4, 5]
b = 4
print(Solution(a, b))

a = [1, 2, 3, 4, 5]
b = 3
print(Solution(a, b))
