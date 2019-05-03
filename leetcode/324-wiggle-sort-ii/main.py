"""
    1st approach: sort similar to lc280
    - sort it, and then split them and put the numbers back to the array

    e.g. even
    [1,3,2,2] 
    
    1. sort
    => [1,2,2,3] < if we do it like lc280, we will have [1,2,2,3] as a result
    
    2. split 
    => [1,2], [2,3]
    
    3. reverse 2nd/stackpop
    => [2,1], [3,2]
    reason: we want to make sure that the end of the 1st half wont collide with the start of the 2nd half, in this case, the 2

    4. result
    [2,3,1,2]

    Time    O(nlogn)
    Space   O(n)
    172 ms, faster than 42.69%
"""


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        clone = sorted(nums)
        halfIdx = (len(nums)+1)/2
        a = clone[:halfIdx]
        b = clone[halfIdx:]
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = a.pop()
            else:
                nums[i] = b.pop()


"""
    suggested approach: quick select, best O(n)
    but i dont think i can come up with this in a 30min interview
    I cant even understand the
"""
