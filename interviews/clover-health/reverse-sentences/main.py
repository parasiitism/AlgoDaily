# This is Python 2
import sys

# line = sys.stdin.readline()
# print line


def reverse(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


t = int(input())
for i in range(t):
    a = raw_input()
    words = a.split()
    reverse(words)
    print(' '.join(words))
