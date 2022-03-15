
def f():
    # input() reads a string with a line of input, stripping the ' ' (newline) at the end
    n, h = map(int, input().split())
    people = [int(s) for s in input().split(" ")]
    res = 0
    for p in people:
        if p <= h:
            res += 1
        else:
            res += 2
    return res


print(f())
