"""
    approach 1a: hashtable, wrap 2sum with one more loop
	1. sort the numbers to make sure that the key will be unique
	2. put the numbers in a hashtable, num:index as key:value
	3. for each nums[i] + nums[j], find out the num from the hashtable that they sum up to zero
	4. use a set to deduplicate

	Time	O(NlogN + N^2 + N) => O(N^2)
	Space	O(N)
	3049ms beats 24.27%
"""


class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        res = set()
        for i in range(n):
            x = nums[i]
            target = 0-x
            ht = defaultdict(int)
            for j in range(i+1, n):
                y = nums[j]
                if target-y in ht:
                    k = ht[target-y]
                    res.add((x, nums[k], y))
                ht[y] = j
        return list(res)


a = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(a))

a = [-2, 0, 1, 1, 2]
print(Solution().threeSum(a))

a = [-13, 5, 13, 12, -2, -11, -1, 12, -3, 0, -3, -7, -7, -5, -3, -15, -2, 14, 14, 13, 6, -11, -11, 5, -15, -14, 5, -5, -2, 0, 3, -8, -10, -7, 11, -5, -10, -5, -7, -6, 2, 5, 3, 2, 7, 7, 3, -10, -2, 2, -12, -11, -1,
     14, 10, -9, -15, -8, -7, -9, 7, 3, -2, 5, 11, -13, -15, 8, -3, -7, -12, 7, 5, -2, -6, -3, -10, 4, 2, -5, 14, -3, -1, -10, -3, -14, -4, -3, -7, -4, 3, 8, 14, 9, -2, 10, 11, -10, -4, -15, -9, -1, -1, 3, 4, 1, 8, 1]
print(Solution().threeSum(a))

print("-----")

"""
    2nd approach: 2 pointers + hashtable
	1. sort the numbers to make sure that the key will be unique
	2. for each num[i], use 2 pointers, from the front and from the end, to find the pairs which nums[i]+nums[j]+nums[k] sum up to 0
	3. use a set to deduplicate

	Time	O(N^2)
	Space	O(N)
	1880 ms, faster than 16.17%
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        resSet = set()
        for i in range(len(nums)):
            num = nums[i]
            target = -num
            left = i+1
            right = len(nums) - 1
            while left < right:
                cur = nums[left] + nums[right]
                if cur == target:
                    resSet.add((num, nums[left], nums[right]))
                if cur > target:
                    right -= 1
                else:
                    left += 1
        return [list(x) for x in resSet]


a = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(a))

a = [-2, 0, 1, 1, 2]
print(Solution().threeSum(a))

a = [-13, 5, 13, 12, -2, -11, -1, 12, -3, 0, -3, -7, -7, -5, -3, -15, -2, 14, 14, 13, 6, -11, -11, 5, -15, -14, 5, -5, -2, 0, 3, -8, -10, -7, 11, -5, -10, -5, -7, -6, 2, 5, 3, 2, 7, 7, 3, -10, -2, 2, -12, -11, -1,
     14, 10, -9, -15, -8, -7, -9, 7, 3, -2, 5, 11, -13, -15, 8, -3, -7, -12, 7, 5, -2, -6, -3, -10, 4, 2, -5, 14, -3, -1, -10, -3, -14, -4, -3, -7, -4, 3, 8, 14, 9, -2, 10, 11, -10, -4, -15, -9, -1, -1, 3, 4, 1, 8, 1]
print(Solution().threeSum(a))

print("-----")


"""
    3rd approach: 2 pointers without hashtable
    
    who to dedup:
    1. skip if nums[i] == nums[i-1]
    2. when we move the pointers
        - imagine [1,1,2,3,4,4], target 5
	    - we need to skip the 1(index 1) and 4(index 4) and check if 2+3 = 5
	
    ref:
    - - https://leetcode.com/problems/3sum/discuss/7380/Concise-O(N2)-Java-solution

	Time	O(N^2)
	Space	O(N)
	652 ms, faster than 76.36%
"""


class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    # deduplicate
                    while j+1 < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k-1 and nums[k-1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
        return res


a = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(a))

a = [-2, 0, 1, 1, 2]
print(Solution().threeSum(a))

a = [-13, 5, 13, 12, -2, -11, -1, 12, -3, 0, -3, -7, -7, -5, -3, -15, -2, 14, 14, 13, 6, -11, -11, 5, -15, -14, 5, -5, -2, 0, 3, -8, -10, -7, 11, -5, -10, -5, -7, -6, 2, 5, 3, 2, 7, 7, 3, -10, -2, 2, -12, -11, -1,
     14, 10, -9, -15, -8, -7, -9, 7, 3, -2, 5, 11, -13, -15, 8, -3, -7, -12, 7, 5, -2, -6, -3, -10, 4, 2, -5, 14, -3, -1, -10, -3, -14, -4, -3, -7, -4, 3, 8, 14, 9, -2, 10, 11, -10, -4, -15, -9, -1, -1, 3, 4, 1, 8, 1]
print(Solution().threeSum(a))

print("-----")

print([3, 5, 7] == [3, 5, 7])
print([3, 5, 7] == [3, 5, 8])

print([[-1, -1, 2], [-1, 0, 1]] == [[-1, -1, 2], [-1, 0, 1]])
print([[-1, -1, 2], [-1, 0, 1]] == [[-1, -1, 2], [-1, 0, 2]])

print({'a': 1, 'b': 2, 'c': 3} == {'a': 1, 'b': 2, 'c': 3})
print({'a': 1, 'b': 2, 'c': 3} == {'a': 1, 'b': 2, 'c': 4})

print({'a', 'b', 'c'} == {'a', 'b', 'c'})
print({'a', 'b', 'c'} == {'a', 'b', 'd'})

assert [3, 5, 7] == [3, 5, 7]
assert [[-1, -1, 2], [-1, 0, 1]] == [[-1, -1, 2], [-1, 0, 1]]
assert {'a': 1, 'b': 2, 'c': 3} == {'a': 1, 'b': 2, 'c': 3}
assert {'a', 'b', 'c'} == {'a', 'b', 'c'}
