"""
    1st approach: brute force
    
    Time    O(n)
    Space   O(1)
    Result 57/100
    https://app.codility.com/demo/results/trainingVDUVVF-URZ/
"""


def solution(N):
    # write your code in Python 3.6
    res = 0
    for i in range(1, N+1):
        if N % i == 0:
            res += 1
    return res


print(solution(24))
print(solution(97))
print(solution(98))

print("-----")

"""
    2nd approach: square

    Time    O(sqrt(n))
    Space   O(1)
    Result 100/100
    https://app.codility.com/demo/results/trainingBXQ8B2-DAJ/
"""


def solution(N):
    if N == 1:
        return 1
    count = 0
    i = 1  # start from 1
    # num * num < N
    while i*i < N:
        if N % i == 0:
            count += 2
        i += 1
    # square number
    if i*i == N:
        count += 1
    return count


print(solution(24))
print(solution(97))
print(solution(98))
