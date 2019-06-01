"""
    1st: brute force

    Time    O(NA)
    Space   O(N)
    Result 88/100 https://app.codility.com/demo/results/trainingAS5HNG-QB2/
"""


def solution(N, A):
    # write your code in Python 3.6
    maxVal = 0
    arr = N * [0]
    for a in A:
        a = a - 1
        if a >= 0 and a < N:
            arr[a] += 1
            maxVal = max(maxVal, arr[a])
        elif a == N:
            arr = N * [maxVal]
    return arr


A = [3, 4, 4, 6, 1, 4, 4]
print(solution(5, A))

A = [3, 4, 4, 6, 1, 4, 4, 6, 2]
print(solution(5, A))

print("-----")

"""
    2nd: lazy write
    - 1 variable for local max
    - 1 variable for global max

    e.g. [3, 4, 4, 6, 1, 4, 4], 5

    [0, 0, 0, 0, 0] <= 3, res[2] += 1
           ^
    [0, 0, 1, 0, 0] <= 4, res[3] += 1
              ^
    [0, 0, 1, 1, 0] <= 4m res[3] += 1
              ^
    [0, 0, 1, 2, 0] <= 6, globalmax = 2, update globalmax = curMax
              
    [0, 0, 1, 2, 0] <= 1, res[0] = globalmax + 1 because res[0] < globalmax
     ^
    [3, 0, 1, 2, 0] <= 4, res[3] += 1
              ^
    [3, 0, 1, 3, 0] <= 4, res[3] += 1
              ^
    [3, 0, 1, 4, 0] <= 4, res[3] += 1

    Time    O(N+A)
    Space   O(N)
    Result 100/100 https://app.codility.com/demo/results/trainingQ2DTQB-ZGF/
"""


def solution(N, A):
    result = N * [0]  # The list to be returned
    global_max = 0   # The used value in previous max_counter command
    current_max = 0   # The current maximum value of any counter
    for a in A:
        a = a - 1
        if 0 <= a < N:
            # increase(X) command
            if result[a] < global_max:
                # lazy update: update the value which has been accesed
                result[a] = global_max
            result[a] += 1
            if result[a] > current_max:
                current_max = result[a]
        else:
            # max_counter command
            # just record the current maximum value for later write
            global_max = current_max
    for index in range(0, N):
        if result[index] < global_max:
            # This element has never been used/updated after previous
            #     global_max command
            result[index] = global_max
    return result


A = [3, 4, 4, 6, 1, 4]
print(solution(5, A))

A = [3, 4, 4, 6, 1, 4, 4, 6, 2]
print(solution(5, A))
