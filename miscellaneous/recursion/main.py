"""
    CS106B part1
"""


def permute(s):
    def dfs(remain, chosen):
        if len(remain) == 0:
            print(chosen)
        for i in range(len(remain)):
            dfs(remain[:i]+remain[i+1:], chosen+remain[i])
    dfs(s, "")


print(permute("abcd"))

print("-----")

"""
    CS106B part2: print binary
"""


def printBinary(n):
    def dfs(x, chosen):
        if x == 0:
            print(chosen)
            return
        dfs(x-1, chosen+'0')
        dfs(x-1, chosen+'1')
    dfs(n, "")


printBinary(3)


"""
    CS106B part2: print printDecimal
"""


def printDecimal(n):
    def dfs(x, chosen):
        if x == 0:
            print(chosen)
            return
        for i in range(10):
            dfs(x-1, chosen+str(i))
    dfs(n, "")


printDecimal(3)
