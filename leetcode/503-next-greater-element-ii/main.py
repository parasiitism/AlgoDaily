"""
    1st classic approach: stack hashtable
	- classic approach: https://www.youtube.com/watch?v=uFso48YRRao
	- [for duplicates]save the index of a number as well, [num, i], into stack, such that we can know which number it refers to

	Time		O(2n)
	Space		O(n)
	344 ms, faster than 27.63%
"""


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        m = {}
        circler = nums + nums
        for i in range(len(circler)):
            num = circler[i]
            while len(stack) > 0 and num > stack[-1][0]:
                pop, idx = stack.pop()
                key = str(pop) + "^" + str(idx)
                m[key] = num
            stack.append((num, i))
        while len(stack) > 0:
            pop, idx = stack.pop()
            key = str(pop) + "^" + str(idx)
            m[key] = -1

        res = []
        for i in range(len(nums)):
            num = nums[i]
            key = str(num) + "^" + str(i)
            res.append(m[key])
        return res


a = [2, 3, 5, 1, 0, 7, 3, 6]
print(Solution().nextGreaterElements(a))

a = [5, 3, 2, 10, 6, 8, 1, 4, 12, 7, 4]
print(Solution().nextGreaterElements(a))

print("-----")

"""
    2nd classic approach: stack
	- classic approach: https://www.youtube.com/watch?v=uFso48YRRao
	- [for duplicates]save the index of a number as well, [num, i], into stack, such that we can know which number it refers to

	Time		O(n)
	Space		O(n)
	236 ms, faster than 37.05%
"""


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        circler = nums + nums
        res = len(nums) * [-1]
        for i in range(len(circler)):
            num = circler[i]
            while len(stack) > 0 and num > stack[-1][0]:
                pop, idx = stack.pop()
                if idx < len(nums):
                    res[idx] = num
            stack.append((num, i))
        return res


a = [2, 3, 5, 1, 0, 7, 3, 6]
print(Solution().nextGreaterElements(a))

a = [5, 3, 2, 10, 6, 8, 1, 4, 12, 7, 4]
print(Solution().nextGreaterElements(a))
