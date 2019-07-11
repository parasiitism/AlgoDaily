def getPrimes(n):
    if n < 2:
        return []
    arePrimes = (n+1)*[True]
    arePrimes[0] = False
    arePrimes[1] = False
    res = []
    for i in range(2, n+1):
        if arePrimes[i] == True:
            res.append(i)
            j = 2
            while i*j < n+1:
                arePrimes[i*j] = False
                j += 1
    return res


def getSemiPrimes(n):
    primes = getPrimes(n)
    res = []
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            p = primes[i]
            q = primes[j]
            if p*q > n:
                break
            res.append(p*q)
    return res


"""
    approach: prime + prefix sum
    - get all the semiprimes in O(N)
    - calculate the prefixsum of semiprimes count for each number, from 0 to N
    
    index:        0  1  2  3  4  5  6  7  8  9  10 ...                                           26
    prefixsums:   [0, 0, 0, 0, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 6, 6, 6, 7, 8, 8, 8, 9, 10]

    Time    O(N^2 + N + P)
    result 100/100
    https://app.codility.com/demo/results/training935C7T-8ZT/
"""


def Solution(N, P, Q):
    if N < 4:
        return [0]
    semiPrimes = set(getSemiPrimes(N))
    pfs = [0]
    for i in range(1, N+1):
        if i in semiPrimes:
            pfs.append(pfs[i-1] + 1)
        else:
            pfs.append(pfs[i-1])
    res = []
    for i in range(len(P)):
        if P[i] <= Q[i]:
            temp = pfs[Q[i]] - pfs[P[i]-1]
            res.append(temp)
    return res


a = 26
b = [1, 4, 16, 5]
c = [26, 10, 20, 10]
print(Solution(a, b, c))

a = 1
b = [1, 4, 16, 5]
c = [26, 10, 20, 10]
print(Solution(a, b, c))

a = 2
b = [1, 4, 16, 5]
c = [26, 10, 20, 10]
print(Solution(a, b, c))
