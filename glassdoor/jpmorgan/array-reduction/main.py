from heapq import *

"""
    Given an array, you need to reduce the number of items by choosing any 2 indices, and the cost is the items are those indices.
    Return the minimum cost to reduce the array to only have only 1 item

    Time    O(NlogN)
    Space   O(N) 
"""


def f(A):
    heapify(A)
    total_cost = 0
    while len(A) > 1:
        a = heappop(A)
        b = heappop(A)
        c = a + b
        total_cost += c
        heappush(A, c)
    return total_cost


print(f([1, 2, 3, 4]))
