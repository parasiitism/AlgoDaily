# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
    1st approach: stack + hashtable
    - similar to lc503

    Time    O(4n)
    Space   O(n)
    480 ms, faster than 6.79%
"""


class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        nums = []
        cur = head
        while cur != None:
            nums.append(cur.val)
            cur = cur.next
        # declaration
        stack = []
        m = {}
        for i in range(len(nums)):
            num = nums[i]
            while len(stack) > 0 and num > stack[-1][0]:
                pop, idx = stack.pop()
                key = str(pop) + "^" + str(idx)
                m[key] = num
            stack.append((num, i))
        # the items in stack dont have next greater
        while len(stack) > 0:
            pop, idx = stack.pop()
            key = str(pop) + "^" + str(idx)
            m[key] = 0
        # iterate the array to consturct the result
        res = []
        for i in range(len(nums)):
            num = nums[i]
            key = str(num) + "^" + str(i)
            res.append(m[key])
        return res


"""
    2nd approach: stack
    - similar to lc503

    Time    O(2n)
    Space   O(n)
    344 ms, faster than 94.64%
"""


class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        nums = []
        cur = head
        while cur != None:
            nums.append(cur.val)
            cur = cur.next
        # declaration
        stack = []
        res = len(nums) * [0]
        for i in range(len(nums)):
            num = nums[i]
            while len(stack) > 0 and num > stack[-1][0]:
                pop, idx = stack.pop()
                res[idx] = num
            stack.append((num, i))
        return res
