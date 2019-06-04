"""
    You are given an array A of non-negative N integers, return the shortest binarian which has the same value as array A.

    Definition of Binarian:

    Binarian = 2^A[0] + 2^A[1] + 2^A[2] + ... + 2^A[N-1] = a value

    e.g. Binarian of 17 can be represeted as [2, 0, 1, 3, 1] = 2^2 + 2^0 + 2^1 + 2^3 + 2^1 = 17

    The shortest Binarian of the value represent as a binarian will be [4, 1] because = [4, 1] = 2^4 + 2^1 = 17

    Note that:
    - 0 <= size if array < 10,000
    - 0 <= each element in array A < 10,000
    - the order of the binarian doesn't matter, e.g. [4, 1] and [1, 4] are both correct
"""


def addBinary(a, b):
    res = []
    carry = 0
    while len(a) > 0 or len(b) > 0:
        x = 0
        if len(a) > 0:
            x = a.pop()
        y = 0
        if len(b) > 0:
            y = b.pop()
        temp = x + y + carry
        res.append(temp % 2)
        carry = temp/2
    if carry > 0:
        res.append(1)
    return res[::-1]


def shortestBinarian(binarian):
    # do binary addition
    binaryRep = []
    for num in binarian:
        binaryRep = addBinary(binaryRep, [1]+num*[0])
    # find the shortest binarian
    shortestBinarian = []
    i = 0
    while len(binaryRep) > 0:
        pop = binaryRep.pop()
        if pop == 1:
            shortestBinarian.append(i)
        i += 1
    return shortestBinarian[::-1]


print(shortestBinarian([2, 0, 1, 3, 1]))
print(shortestBinarian([1, 1, 1, 1, 1, 1, 1, 1]))
print(shortestBinarian([1, 0, 2, 0, 0, 2]))
print(shortestBinarian([3, 2, 0]))
