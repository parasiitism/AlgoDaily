"""
    Given a snippet of lines of code, calculate the length of the code which is non-comment and non-whitespace

    There are 2 types of comments:
    - line comment: start with // until the end of the line
    - block comment: start with /* and end with */
    
    You don't have to worry about // or /* or */ inside a string literal
"""


def f(source):
    N = len(source)
    is_comment = False
    res = 0
    for i in range(N):
        line = source[i]
        L = len(line)
        j = 0
        while j < L:
            if line[j] == '/' and j+1 < L and line[j+1] == '/' and is_comment == False:
                j = L
            elif line[j] == '/' and j+1 < L and line[j+1] == '*' and is_comment == False:
                is_comment = True
                j += 1
            elif line[j] == '*' and j+1 < L and line[j+1] == '/' and is_comment == True:
                is_comment = False
                j += 1
            elif line[j] != ' ' and is_comment == False:
                res += 1
            j += 1
    return res


a = [
    'int a = 2;',
    'int b = 47;/*37;*///41;',
    'int c = 3/*4//5*/;',
    'return a / b * c/*a /* b / c*/;'
]
print(f(a))
