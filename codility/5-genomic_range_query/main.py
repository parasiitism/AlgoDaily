"""
    1st approach: prefix min
    - generate all combinations, get the min impact between the combinations
    - for every pair, P and Q, get the min impact from the hashtable

    Time    O(n^2 + m)
    Space   O(n^2)
    Result 60/100 https://app.codility.com/demo/results/trainingESRERC-CTN/
"""


def solution(S, P, Q):
    # write your code in Python 3.6
    impacts = {
        'A': 1,
        'C': 2,
        'G': 3,
        'T': 4,
    }
    m = {}
    for i in range(len(S)):
        prefixMin = 5
        for j in range(i, len(S)):
            prefixMin = min(prefixMin, impacts[S[j]])
            m[(i, j)] = prefixMin

    res = []
    for i in range(len(P)):
        a, b = P[i], Q[i]
        key = (a, b)
        res.append(m[key])
    return res


a = "CAGCCTA"
b = [2, 5, 0]
c = [4, 5, 6]
print(solution(a, b, c))

print("-----")

"""
    2nd approach: hastable
    - for every pair, P and Q, find if there is a character A, C, G or T in the substring

    ref:
    - more detail please check it out at https://codesays.com/2014/solution-to-genomic-range-query-by-codility/#comment-1727 .

    Time    O(m(n+4))
    Space   O(m)
    Result 100/100 https://app.codility.com/demo/results/trainingMUJ4YG-UBZ/
"""


def solution(S, P, Q):

    impacts = {
        'A': 1,
        'C': 2,
        'G': 3,
        'T': 4,
    }
    keys = ['A', 'C', 'G', 'T']

    res = []
    for i in range(len(P)):
        p, q = P[i], Q[i]
        sub = S[p:q+1]
        for num in range(4):
            key = keys[num]
            if key in sub:
                res.append(impacts[key])
                break
    return res


a = "CAGCCTA"
b = [2, 5, 0]
c = [4, 5, 6]
print(solution(a, b, c))
