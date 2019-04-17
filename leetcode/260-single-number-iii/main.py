"""
    1st approach: hashtable

    Time    O(n)
    Space   O(n)
    48ms beats 42.29%
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ht = {}
        for num in nums:
            if num not in ht:
                ht[num] = 1
            else:
                ht[num] += 1
        res = []
        for key in ht:
            if ht[key] == 1:
                res.append(key)
        return res


print(Solution().singleNumber([1, 2, 1, 3, 2, 5]))

print("--------------------")

"""
    2nd approach: bit operation

    1. first run ^ to get the a^b
    2. search the position to do partitioning in binary representation of a^b 
    3. partition the array by this position and get a and b correspondingly

    e.g. [1,2,1,3,2,5]

    1 = 001
    2 = 010
    1 = 001
    3 = 011
    2 = 010
    5 = 101

    after 1st step, we found out 3^5 = 6 which is 110
    110 means that there are 2 digits on the left are different in binary representation of our result
    let's use any one of the digit to partition our array

    if we use the middle one, we can see that there are 2 sets of numbers that we can just use the simple single number to find out the single in each partition
    1 = 001
    1 = 001
    5 = 101
    -------
    2 = 010
    2 = 010
    3 = 011

    if we use the leftmost one, we can still partition the array into the sets and do simple single number on it
    1 = 001
    2 = 010
    1 = 001
    3 = 011
    2 = 010
    -------
    5 = 101

    ref:
    - see ./idea.png (from http://yucoding.blogspot.com/2016/12/leetcode-question-single-number-iii.html)

    Time    O(n)
    Space   O(1) 
    48 ms, faster than 42.29%
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # get the a^b first
        ab = 0
        for num in nums:
            ab ^= num
        # get the digit for partitioning
        mask = 1
        a = b = ab
        while (ab & mask == 0):
            mask = mask << 1
        # do partition
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        return [a, b]


print(Solution().singleNumber([1, 2, 1, 3, 2, 5]))
