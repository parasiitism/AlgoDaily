"""
    Basically, we can use mode(%) to determine which string we are going to use, 
    we can do it by iterating an increment value cnt
    if i%2==0 use a
    if i%2==1 use b
    if there is nothing we can extract from a string, just increment cnt and go to the next iteration
"""


def mergeStrings(a, b):
    cnt = 0
    res = ""
    while len(a) > 0 or len(b) > 0:
        if cnt % 2 == 0:
            if len(a) > 0:
                res += a[0]
                a = a[1:]
        else:
            if len(b) > 0:
                res += b[0]
                b = b[1:]
        cnt += 1
    return res


# normal case
print(mergeStrings("abcd", "efgh"))
# normal case
print(mergeStrings("ab", "efgh"))
# normal case
print(mergeStrings("abcd", "ef"))

# corner case
print(mergeStrings("", "efgh"))
# corner case
print(mergeStrings("abcd", ""))
# corner case
print(mergeStrings("", ""))
