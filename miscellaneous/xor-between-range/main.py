"""
    Find the product of XORs in a given range of ints.

    e.g.
    (5,8)

    => 5 XOR 6 XOR 7 XOR 8 ( bitwise xor )
    => 12

    where M <= N, 
    M <= N <= 1,000,000,000
"""


"""
    Actually when we run from 0 to n, there is a pattern

    a is the index
    0   0000 <- 0  [a]
    1   0001 <- 1  [1]
    2   0010 <- 3  [a+1]
    3   0011 <- 0  [0]
    4   0100 <- 4  [a]
    5   0101 <- 1  [1]
    6   0110 <- 7  [a+1]
    7   0111 <- 0  [0]
    8   1000 <- 8  [a]
    9   1001 <- 1  [1]
    10  1010 <- 11 [a+1]
    11  1011 <- 0  [0]
    12  1100 <- 12 [a]
    13  1101 <- 1  [1]
    14  1110 <- 15 [a+1]
    15  1111 <- 0  [0]
"""


def f(n):
    pattern = [n, 1, n+1, 0]
    return pattern[n % 4]


"""
    Since a number XOR itself becomes 0, we can calculate the range by f(M - 1) ^ f(N)

    e.g.
    5^8
    
    a = 0^1^2^3^4
    b = 0^1^2^3^4^5^6^7^8

    a^b = 5^6^7^8 because 0^1^2^3^4 in b has been canceled out by a0^1^2^3^4

    therefore, we can calcuate getXorBetween(5,8) by just f(4)^f(8)
"""


def getXorBetween(a, b):
    return f(a-1) ^ f(b)


print(getXorBetween(5, 8))
