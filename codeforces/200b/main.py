
def f():
    n = int(input())
    nums = [int(s) for s in input().split(" ")]
    total = 0
    for x in nums:
        total += x
    return total / n


print(f())
