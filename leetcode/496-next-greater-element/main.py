"""
    2st approach: stack + hashtable
    - the stack only stores the smaller items n the top
    - so when we iterate through the nums, if current num > stack.top(), put the current num is the next greater number of stack.top()
    - do step 2 in a loop
    - after we have done step2,3, if we still have numbers in the stack, it means that they dont have the next greater number

    Time    O(2n + m) m:nums1, n:nums2
    Space   O(n)
    36 ms, faster than 72.26%
"""


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        m = {}
        for num in nums2:
            while len(stack) > 0 and num > stack[-1]:
                pop = stack.pop()
                m[pop] = num
            stack.append(num)
        while len(stack) > 0:
            pop = stack.pop()
            m[pop] = -1
        res = []
        for num in nums1:
            res.append(m[num])
        return res
