"""
    Math

    e.g.1
    Input: arr[] = {1, 2, 3}
    Output: 20
    Explanation: {1} + {2} + {3} + {2 + 3} + {1 + 2} + {1 + 2 + 3} = 20

    e.g.2
    Input: arr[] = {1, 2, 3, 4}
    Output: 50

    Solution:
    - instead of generate all the subarrays in O(N^2), try to think that the how many subarrays will include arr[i]

    https://www.geeksforgeeks.org/sum-of-all-subarrays/
"""


def f(arr):
    n = len(arr)
    res = 0
    for i in range(n):
        subarrays_start_from_i = n - i
        subarrays_include_i = i * (n-i)
        res += arr[i] * (subarrays_start_from_i + subarrays_include_i)
    return res


a = [1, 2, 3]
print(f(a))

a = [1, 2, 3, 4]
print(f(a))
