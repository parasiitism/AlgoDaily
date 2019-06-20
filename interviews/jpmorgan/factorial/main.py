"""
    no negative? yes
"""


# recursion
def f(num):
    if num < 0:
        return -1  # actually it should be infinity
    if num == 0:
        return 1
    return num*f(num-1)


print(f(-2))
print(f(4))
print(f(5))
print(f(10))
print("-----")

# iteration


def f(num):
    if num < 0:
        return -1  # actually it should be infinity
    res = 1
    for i in range(1, num+1):
        res *= i
    return res


print(f(-2))
print(f(4))
print(f(5))
print(f(10))
print("-----")
