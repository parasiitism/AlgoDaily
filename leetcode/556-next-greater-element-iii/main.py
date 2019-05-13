"""
    classic approach: Next lexicographical permutation algorithm(use a stack)

    similar to lc31

	e.g. 43143221
	- find the non-increasing suffix, e.g. 431<43221>
	- once it encounters a smaller number from the end, this is the target we want
		e.g. 43 <1> 43221
	- i need to swap the target with the value in the stack which is just larger then it
		e.g. 43 <1> 43221
                       ^
         => 43 <2> 43211
                      ^
	- reverse the right half and put it back to the number
		e.g. 43 <2> 43211 => 43 <2> 11234
	- combine them together and form the result
		e.g. 43 <2> 11234 => 43211234

	ref:
	- https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

	Time	O(n)
	Space	O(n)
	8 ms, faster than 100.00%
"""


class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return -1
        # transform the digits to an array
        nums = []
        while n > 0:
            nums = [n % 10] + nums
            n /= 10
        # find the pivot from the increasing sequence from the right
        pivot = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        # if no pivot, return fail to get the next one
        if pivot == -1:
            return -1
        # find the number to swap
        target = -1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[pivot]:
                target = i
                break
        # swap
        nums[pivot], nums[target] = nums[target], nums[pivot]
        # reverse the increasing sequence from the right
        self.reverse(nums, pivot+1, len(nums)-1)
        # transform back to an integer
        res = 0
        for num in nums:
            res = res*10 + num
        # check range
        if res > 2**31-1:
            return -1
        return res

    def reverse(self, nums, start, end):
        left = start
        right = end
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


print(Solution().nextGreaterElement(12))
print(Solution().nextGreaterElement(21))
print(Solution().nextGreaterElement(312))
print(Solution().nextGreaterElement(43143221))
print(Solution().nextGreaterElement(1999999999))
print(Solution().nextGreaterElement(0))
print(Solution().nextGreaterElement(1))
