"""
    1st approach: hashtable
    - add the numbers to a hashset
    - if we see a number from A, remove that number from hashset
    - the result is the index where we removed all the items from the hashset

    Time    O(n)
    Space   O(n)
    result 100/100 https://app.codility.com/demo/results/trainingT8S544-9YR/
"""


def solution(X, A):
    # write your code in Python 3.6
    hs = set()
    for i in range(1, X+1):
        hs.add(i)
    for i in range(len(A)):
        a = A[i]
        if a in hs:
            hs.remove(a)
        if len(hs) == 0:
            return i
    return -1


print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
print(solution(6, [1, 3, 1, 4, 2, 3, 5, 4]))
