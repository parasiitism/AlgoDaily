"""
    Given an array of N integers, return the triangle with the minimal perimeter
    Triangle inequality should be respected among the three values of the triangle:
    a+b>c
    a+c>b
    b+c>a
"""


def f(nums):
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            if check(nums[i], nums[j], nums[j+1]):
                return nums[i] + nums[j] + nums[j+1]
    return -1


def check(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


a = [1, 2, 3, 4, 5, 6, 7, 8]
print(f(a))
