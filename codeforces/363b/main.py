"""
    sliding window
    
    Time    O(N)
    Space   O(1)
"""


def f():
    n, width = [int(x) for x in input().split()]
    fences = [int(x) for x in input().split()]
    window_sum = 0
    min_window_sum = 2**32
    res = -1
    for i in range(n):
        window_sum += fences[i]
        if i >= width:
            window_sum -= fences[i-width]
        if i >= width-1:
            if window_sum < min_window_sum:
                res = i - width + 1
                min_window_sum = window_sum
    print(res+1)  # 1-indexed


f()
