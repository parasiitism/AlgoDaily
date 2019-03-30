# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
    2nd approach: dont count the linked list in constructor, do it in getRandom()

    Time  O(1) constructor(), O(n) getRandom()
    Space O(n)
    92 ms, faster than 67.61%
"""


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        cnt = 0
        cur = self.head
        while cur != None:
            cnt += 1
            cur = cur.next
        node = self.head
        r = random.randrange(cnt)
        for _ in range(r):
            node = node.next
        return node.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
