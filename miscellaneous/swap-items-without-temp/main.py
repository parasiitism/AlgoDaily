"""
    Swap integers

    dont use
    a, b = b, a

    a = 3, b = 10
    a = a + b = 3 + 10  = 13
    b = a - b = 13 - 10 = 3
    a = a - b = 13 - 3  = 10
    a = 10, b = 3
"""


def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


a = 3
b = 10
print(swap(a, b))

print("-----")

"""
    3(11), 10(1010)

    a = a^b
          11
    ^   1010
    --------
        1001
    
    b = a^b
        1001
    ^   1010
    --------
          11
    
    a = a^b
        1001
    ^     11
    --------
        1010

    
"""


def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


a = 3
b = 10
print(swap(a, b))


"""
    swap string
"""


def swap(a, b):
    a = a + b
    b = a[:len(a)-len(b)]
    a = a[len(b):]
    return a, b


a = "a"
b = "bc"
print(swap(a, b))
