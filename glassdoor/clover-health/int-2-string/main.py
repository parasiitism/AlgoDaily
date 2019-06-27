def int2string(n):
    res = ''
    i = 0
    while n > 0:
        temp = n % 10
        n /= 10
        res = str(temp) + res
        if n != 0 and (i+1) % 3 == 0:
            res = ',' + res
        i += 1
    return res


print(int2string(99))
print(int2string(199))
print(int2string(2199))
print(int2string(123199))
print(int2string(1234199))
print(int2string(991234199))
print(int2string(1991234199))
