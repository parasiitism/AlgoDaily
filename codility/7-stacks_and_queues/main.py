"""
    1st approach: similar to lc20

    Time    O(n)
    Space   O(1)
    Result 100/100 https://app.codility.com/demo/results/trainingTGZ4UQ-6YP/
"""


def solution(S):
    # write your code in Python 3.6
    openCnt = 0
    for c in S:
        if c == '(':
            openCnt += 1
        elif c == ')':
            if openCnt == 0:
                return 0
            else:
                openCnt -= 1
    return 1 if openCnt == 0 else 0
