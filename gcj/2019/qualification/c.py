"""
2
103 31
217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053
10000 25
3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543

Output

Case #1: CJQUIZKNOWBEVYOFDPFLUXALGORITHMS
Case #2: SUBDERMATOGLYPHICFJKNQVWXZ
"""


def getPrimes(n):
    if n < 2:
        return []
    res = []
    notPrime = n*[False]
    for i in range(2, n):
        if notPrime[i] == False:
            res.append(i)
            j = 2
            while i*j < n:
                notPrime[i*j] = True
                j += 1
    return res


def bsearch(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right)/2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def cryptopangram(n, nums):
    primes = getPrimes(n+1)
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # find the first and second numbers
    if len(nums) == 0:
        return ""
    first = nums[0]
    i = 0
    buffero = 0
    while i < len(primes):
        buffero = float(first/float(primes[i]))
        if buffero != int(buffero):
            i += 1
        else:
            buffero = int(buffero)
            break

    indeces = []
    # ps = []
    firstNum = primes[i]

    # get the index of first number in prime numbers
    firstIdx = bsearch(primes, firstNum)
    if firstIdx > -1:
        indeces.append(firstIdx)
        # ps.append(firstNum)

    # get the index of second number in prime numbers
    bufferIdx = bsearch(primes, buffero)
    if bufferIdx > -1:
        indeces.append(bufferIdx)
        # ps.append(buffero)

    # start to find the upcoming prime numbers
    for i in range(1, len(nums)):
        num = nums[i]
        buffero = int(num/buffero)
        # ps.append(buffero)
        bufferIdx = bsearch(primes, buffero)
        if bufferIdx > -1:
            indeces.append(bufferIdx)

    # sort the seen prime numbers
    clone = indeces[:]
    sortedIndeces = sorted(list(set(clone)))

    # for each prime, get the index in prime numbers
    res = ""
    for primeIdx in indeces:
        pos = bsearch(sortedIndeces, primeIdx)
        res += alphabets[pos]

    return res


# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    a = [int(s) for s in raw_input().split(" ")]
    b = [int(s) for s in raw_input().split(" ")]
    try:
        c = cryptopangram(a[0], b)
        print("Case #{}: {}".format(i, c))
    except:
        print("Case #{}: {}".format(i, ""))
