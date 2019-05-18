"""
    1st approach: 
    - for float, get the 2 most significant digit
    - for int, divide the number 1000 repeatedly until 0
"""


def numberToCurrency(num):
    # floating number
    f = num - int(num)
    fn = int(round(100*f))
    ffn = ''
    if fn == 0:
        ffn = '00'
    elif fn < 10:
        ffn = '0' + str(fn)
    else:
        ffn = str(fn)
    # decimal number
    arr = []
    cur = int(num)
    while cur > 0:
        arr.append(str(cur % 1000))
        cur /= 1000
    intn = ""
    if len(arr) > 0:
        intn = ','.join(arr[::-1])
    else:
        intn = '0'

    return intn + '.' + ffn


print(numberToCurrency(1234.678))
print(numberToCurrency(12345.678))
print(numberToCurrency(123456789.678))
print(numberToCurrency(1234567899.678))
print(numberToCurrency(123456789.01))
print(numberToCurrency(123456789.009))
print(numberToCurrency(0.678))
print(numberToCurrency(0.648))
print(numberToCurrency(0.01))
print(numberToCurrency(0.10))
print(numberToCurrency(0.0099))
print(numberToCurrency(0))

print("-----")

"""
    2nd approach: 
    - use built-in helper
"""


def numberToCurrency(num):
    return '{:,.2f}'.format(num)


print(numberToCurrency(1234.678))
print(numberToCurrency(12345.678))
print(numberToCurrency(123456789.678))
print(numberToCurrency(1234567899.678))
print(numberToCurrency(123456789.01))
print(numberToCurrency(123456789.009))
print(numberToCurrency(0.678))
print(numberToCurrency(0.648))
print(numberToCurrency(0.01))
print(numberToCurrency(0.10))
print(numberToCurrency(0.0099))
print(numberToCurrency(0))
