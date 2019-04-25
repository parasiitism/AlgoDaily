"""
    classic approach: Next lexicographical permutation algorithm(use a stack)
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
	20 ms, faster than 67.52%
"""


class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        numStr = str(n)
        nums = []
        for c in numStr:
            nums.append(int(c))

        arr = []
        idx = -1
        for i in range(len(nums)-1, 0, -1):
            arr.append(nums[i])
            if nums[i-1] < nums[i]:
                idx = i
                break
        if idx == -1:
            return -1
        pivot = nums[idx-1]
        for i in range(len(arr)):
            if arr[i] > pivot:
                temp = nums[idx-1]
                nums[idx-1] = arr[i]
                arr[i] = temp
                break
        clone = nums[:idx] + arr
        res = 0
        for i in range(len(clone)):
            res = res*10 + clone[i]
        if res > 2**31-1:
            return -1
        return res


print(Solution().nextGreaterElement(12))
print(Solution().nextGreaterElement(21))
print(Solution().nextGreaterElement(312))
print(Solution().nextGreaterElement(43143221))
print(Solution().nextGreaterElement(1999999999))
print(Solution().nextGreaterElement(0))
print(Solution().nextGreaterElement(1))
