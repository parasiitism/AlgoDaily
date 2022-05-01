def f():
    """
    *
    * *   *
    * * * *
    3 2 1 2

          *
      * * *
    * * * *
    1 2 2 3
    """
    _ = input()
    arr = [int(s) for s in input().split(" ")]
    arr.sort()
    return " ".join([str(x) for x in arr])


print(f())
