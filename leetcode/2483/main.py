"""
    1st: prefix sum, suffix sum
    - 2 arrays to store the number of Ns and Ys: forward, backward

    Time    O(3N)
    Space   O(2N)
    1033 ms, faster than 20.64%
"""


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        forward_Ns = (n+2) * [0]
        backward_Ys = (n+2) * [0]

        Ns = 0
        for i in range(n):
            if customers[i] == 'N':
                Ns += 1
            forward_Ns[i+1] = Ns

        Ys = 0
        for i in range(n-1, -1, -1):
            if customers[i] == 'Y':
                Ys += 1
            backward_Ys[i+1] = Ys

        min_idx = -1
        min_penalty = 2**32
        for i in range(1, n+2):
            temp = forward_Ns[i-1] + backward_Ys[i]
            if temp < min_penalty:
                min_penalty = temp
                min_idx = i
        return min_idx-1


"""
    2nd: optimize the 1st

    Time    O(2N)
    Space   O(2N)
    1170 ms, faster than 16.72%
"""


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        forward_Ns = (n+2) * [0]
        backward_Ys = (n+2) * [0]

        Ns = 0
        Ys = 0
        for i in range(n):
            # from left to right
            if customers[i] == 'N':
                Ns += 1
            forward_Ns[i+1] = Ns
            # from right to left
            j = n-i-1
            if customers[j] == 'Y':
                Ys += 1
            backward_Ys[j+1] = Ys

        min_idx = -1
        min_penalty = 2**32
        for i in range(1, n+2):
            temp = forward_Ns[i-1] + backward_Ys[i]
            if temp < min_penalty:
                min_penalty = temp
                min_idx = i
        return min_idx-1
