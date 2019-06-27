"""
    Given a linked list represented by an array, find the length of the linked list

    Representation:
    A[0] -> A[A[0]] -> A[A[A[0]]] -> .... -> A[...] the value of the last item is -1 
"""


def lengthOfLinkedList(A):
    count = 0
    i = 0
    while A[i] > -1:
        i = A[i]
        count += 1
    return count


print(lengthOfLinkedList([2, 4, 1, 3, -1, 0]))
print(lengthOfLinkedList([2, 4, 1, -1, 5, 3]))
