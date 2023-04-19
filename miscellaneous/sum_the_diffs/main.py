"""
    Sum all the absolute diffs between every element in an integer array

    e.g. 
    [0, 3, 2, 9, 11]

    At idx=0, |3-0| + |2-0| + |9-0| + |11-0| = 25
    At idx=1, |0-3| + |2-3| + |9-3| + |11-3| = 18
    At idx=2, |0-2| + |3-2| + |9-2| + |11-2| = 19
    At idx=3, |0-9| + |3-9| + |2-9| + |11-9| = 24
    At idx=4, |0-11| + |3-11| + |2-11| + |9-11| = 30
    
    resu;t = 25 + 18 + 19 + 24 + 30 = 116
"""


def bruteforce(A):
    """
        Time    O(N^2)
        Space   O(1)
    """
    n = len(A)
    res = 0
    for i in range(n):
        for j in range(n):
            res += abs(A[i] - A[j])
    return res


a = [0, 2, 3, 5]
print(bruteforce(a))

a = [0, 3, 2, 9, 11]
print(bruteforce(a))

a = [6, 7, 8, 97, 6, 5, 6, 7, 54, 8, 3, 3, 2, 9, 11, 3, 4, 5, 9, 20]
print(bruteforce(a))

print("-----")


def sum_the_diffs(A):
    """
        idea:
        |A[0] - A[i]| + |A[1] - A[i]| + ...... |A[i] - A[i]| + ...... + |A[n-2] - A[i]| + |A[n-1] - A[i]|

        if A is sorted, we can remove the absolute by reverting the left hand side to do the same thing:
        (A[i] - A[0]) + (A[i] - A[1]) + ...... (A[i] - A[i]) + ...... + (A[n-2] - A[i]) + (A[n-1] - A[i])

        Time    O(NlogN + N)
        Space   O(N)
    """
    A.sort()
    n = len(A)
    total = sum(A)
    pfss = []
    pfs = 0
    res = 0
    for x in A:
        pfs += x
        pfss.append(pfs)
    for i in range(n):
        left = (i + 1) * A[i] - pfss[i]
        right = total - pfss[i] - (n - i - 1) * A[i]
        res += left + right
    return res


a = [0, 2, 3]
print(sum_the_diffs(a))

a = [0, 3, 2, 9, 11]
print(sum_the_diffs(a))

a = [6, 7, 8, 97, 6, 5, 6, 7, 54, 8, 3, 3, 2, 9, 11, 3, 4, 5, 9, 20]
print(sum_the_diffs(a))
