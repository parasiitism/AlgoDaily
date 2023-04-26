"""
    Question:
    Given R, C, queries, which represent a RxC matrix and the operations below, return the result of the queries.

    3 types of queries
    - (0) - find the minimum value among all remaining active cells on the board
    - (1, i) - deactivate all cells in the row i
    - (2, j) - deactivate all cells in the colum j

    e.g.
    Beginning:
    [
        [1, 2, 3, 4],
        [2, 4, 6, 8],
        [3, 6, 9, 12]
    ]
    query(1,2):
    [
        [1, 2, 3, 4],
        [2, 4, 6, 8], <- this row deactived
        [3, 6, 9, 12]
    ]
    query(0): the result is 1 (the item at M[0][0])
    [
        [1, 2, 3, 4],
        [2, 4, 6, 8],
        [3, 6, 9, 12]
    ]
    query(2, 1):
    [
        [1, 2, 3, 4],
        [2, 4, 6, 8], <
        [3, 6, 9, 12]
         ^
        this row deactived
    ]
    query(0): the result is 2 (the item at M[0][1])
    [
        [1, 2, 3, 4],
        [2, 4, 6, 8],
        [3, 6, 9, 12]
    ]

    video: https://codesignal.s3.amazonaws.com/uploads/19122104111327/14850converted.mp4?tag=1p3a-api-20

    1st: use a linked list
    - Build Time    O(R + C)
    - Remove Time   O(R + C)
    - Get Min Time  O(1)
    - implemented below 

    2nd: use a BST
    - Build Time    O(RlogR + ClogC)
    - Remove Time   O(logR + logC)
    - Get Min Time  O(logR + logC)
    - idea only
"""


class LLNode(object):
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = None


def build_linked_list(n):
    head = LLNode()
    cur = head
    for i in range(1, n+1):
        cur.next = LLNode(i)
        cur = cur.next
    return head


def remove_node_from_linked_list(head, val):
    cur = head
    while cur.next != None:
        if cur.next.val == val:
            cur.next = cur.next.next
            return
        cur = cur.next


def f(R, C, queries):
    row_head = build_linked_list(R)
    col_head = build_linked_list(C)
    res = []
    for q in queries:
        if q[0] == 0:
            if row_head.next != None and col_head.next != None:
                r = row_head.next.val
                c = col_head.next.val
                res.append(r*c)
        elif q[0] == 1:
            val = q[1]
            remove_node_from_linked_list(row_head, val)
        elif q[0] == 2:
            val = q[1]
            remove_node_from_linked_list(col_head, val)
    return res


queries = [
    [0], [1, 2], [0], [2, 1], [0], [1, 1], [0]
]
print(f(3, 4, queries))
