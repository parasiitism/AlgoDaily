from cgi import print_directory
from posixpath import split


def f():
    n = int(input())
    for _ in range(n):
        a, b = [int(c) for c in input().split()]
        if a != b:
            print("Happy Alex")
            return
    print("Poor Alex")


f()
