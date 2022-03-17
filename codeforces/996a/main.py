
def f():
    n = int(input())

    a, n = n//100, n % 100
    b, n = n//20, n % 20
    c, n = n//10, n % 10
    d, n = n//5, n % 5

    return a + b + c + d + n


print(f())
