
# Definition for a Node.


class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next


"""
    classic problem, classic approach
    - find the minNode
    - there are 3 cases to insert a node
        1. cur < target < cur.next
        2. cur == target == cur
        3. cur.next == head and insertion no yet happen

    Time    O(2n)
    Space   O(1)
    460ms beats 98.10%
"""


class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        # if nil
        if head == None:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode

        # find the left most node with min value
        minNode = head
        cur = head
        while True:
            if cur.val < minNode.val:
                minNode = cur
            cur = cur.next
            if cur == head:
                break

        # start to find the place from the minnode
        cur = minNode
        while True:
            if (cur.val < insertVal and insertVal < cur.next.val) \
                    or (cur.next == minNode) \
                    or (insertVal == cur.val):
                newNode = Node(insertVal, cur.next)
                cur.next = newNode
                break
            cur = cur.next

        # return head
        return head


def printList(node):
    cur = node
    res = ""
    while True:
        res += str(cur.val) + ","
        cur = cur.next
        if cur == node:
            break
    print(res)


# 3->4->1 2
three = Node(3, None)
four = Node(4, None)
one = Node(1, None)
three.next = four
four.next = one
one.next = three


s = Solution().insert(three, 2)
printList(s)


# 3->3->3 2
three = Node(3, None)
four = Node(3, None)
one = Node(3, None)
three.next = four
four.next = one
one.next = three


s = Solution().insert(three, 2)
printList(s)

# 1->3->5 0
one = Node(1, None)
three = Node(3, None)
five = Node(5, None)
one.next = three
three.next = five
five.next = one

s = Solution().insert(one, 0)
printList(s)

# 3->5->1 0
three = Node(3, None)
five = Node(5, None)
one = Node(1, None)
three.next = five
five.next = one
one.next = three

s = Solution().insert(three, 0)
printList(s)

# 2->2->3->4->1 2
two1 = Node(2, None)
two2 = Node(2, None)
three = Node(3, None)
four = Node(4, None)
one = Node(1, None)
two1.next = two2
two2.next = three
three.next = four
four.next = one
one.next = two1


s = Solution().insert(two1, 2)
printList(s)

print("--------------------")

"""
    2nd approach: optimize the above approach
    - find the minNode
    - there are 2 cases to insert a node
        1. cur <= target < cur.next
        2. cur.next == head and insertion no yet happen

    Time    O(2n)
    Space   O(1)
    460ms beats 98.10%
"""


class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        # if nil
        if head == None:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode

        # find the left most node with min value
        minNode = head
        cur = head
        while True:
            if cur.val < minNode.val:
                minNode = cur
            cur = cur.next
            if cur == head:
                break

        # start to find the place from the minNode
        cur = minNode
        while True:
            if cur.val <= insertVal and insertVal < cur.next.val:
                cur.next = Node(insertVal, cur.next)
                break
            if cur.next == minNode:
                cur.next = Node(insertVal, cur.next)
                break
            cur = cur.next

        return head


# 3->4->1 2
three = Node(3, None)
four = Node(4, None)
one = Node(1, None)
three.next = four
four.next = one
one.next = three


s = Solution().insert(three, 2)
printList(s)


# 3->3->3 2
three = Node(3, None)
four = Node(3, None)
one = Node(3, None)
three.next = four
four.next = one
one.next = three


s = Solution().insert(three, 2)
printList(s)

# 1->3->5 0
one = Node(1, None)
three = Node(3, None)
five = Node(5, None)
one.next = three
three.next = five
five.next = one

s = Solution().insert(one, 0)
printList(s)

# 3->5->1 0
three = Node(3, None)
five = Node(5, None)
one = Node(1, None)
three.next = five
five.next = one
one.next = three

s = Solution().insert(three, 0)
printList(s)

# 2->2->3->4->1 2
two1 = Node(2, None)
two2 = Node(2, None)
three = Node(3, None)
four = Node(4, None)
one = Node(1, None)
two1.next = two2
two2.next = three
three.next = four
four.next = one
one.next = two1


s = Solution().insert(two1, 2)
printList(s)
