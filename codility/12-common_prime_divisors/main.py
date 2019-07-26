"""
    1st approach: brute force

    Time    O(nm)
    Space   O(n)
    Result 53/100
    https://app.codility.com/demo/results/trainingVUQMM3-V8C/
"""


def solution(A, B):
    primes = getPrimes(46341)
    res = 0
    for i in range(len(A)):
        a = A[i]
        b = B[i]

        primeFactersOfA = ""
        for j in range(len(primes)):
            if a % primes[j] == 0:
                primeFactersOfA += str(primes[j]) + ","

        primeFactersOfB = ""
        for j in range(len(primes)):
            if b % primes[j] == 0:
                primeFactersOfB += str(primes[j]) + ","

        if primeFactersOfA == primeFactersOfB:
            res += 1

    return res


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


"""
    2nd approach: euclidean algorithm to find gcd

    Wrong Answer
"""


def findGcd(a, b):
    if b == 0:
        return a
    return findGcd(b, a % b)


def solution(A, B):
    res = 0
    for i in range(len(A)):
        a = A[i]
        b = B[i]

        gcd = findGcd(a, b)
        if gcd == 1:
            continue

        a_ = a//gcd
        b_ = b//gcd
        if gcd % a_ == 0 and gcd % b_ == 0:
            res += 1

    return res


A = [15, 10, 3]
B = [75, 30, 5]
print(solution(A, B))

A = [15, 10, 3, 30]
B = [75, 30, 5, 150]
print(solution(A, B))
