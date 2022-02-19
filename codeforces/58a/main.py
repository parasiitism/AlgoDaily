from cgi import print_directory


def f():
    s = input()
    hello = 'hello'
    j = 0
    for i in range(len(s)):
        if j < 5 and s[i] == hello[j]:
            j += 1
    if j == 5:
        print('YES')
    else:
        print('NO')


f()
