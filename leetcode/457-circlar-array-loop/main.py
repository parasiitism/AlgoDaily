"""
    1st approach: 2 pointers
    - at each index
        - 1 pointer goes 1 step, another pointer goes 2 steps
        - if there is a loop, they will meet at a point
    - corner cases:
        - 1 item in a loop isnt considered valid
        - loop only goes with one direction

    Time    O(n^2)
    Space   O(1)
    872 ms, faster than 12.65%
"""


class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        agg = False
        for i in range(len(nums)):
            temp = self.detectLoop(nums, i)
            agg = agg or temp
        return agg

    def detectLoop(self, nums, idx):
        n = len(nums)
        slow = idx
        slowGoesForward = True if nums[idx] > 0 else False  # True:+, False:-
        fast = idx
        fastGoesForward = True if nums[idx] > 0 else False  # True:+, False:-
        while True:
            nextSlowGoesForward = True if nums[slow] > 0 else False
            # wont go backward
            if slowGoesForward != nextSlowGoesForward:
                return False
            nextSlow = self.calNextIdx(slow, nums[slow], n)
            # wont be one item loop
            if nextSlow == slow:
                return False
            slow = nextSlow

            nextGoesForward = True if nums[fast] > 0 else False
            # wont go backward
            if fastGoesForward != nextGoesForward:
                return False
            temp = self.calNextIdx(fast, nums[fast], n)

            fastGoesForward = True if nums[temp] > 0 else False
            # wont go backward
            if nextGoesForward != fastGoesForward:
                return False
            fast = self.calNextIdx(temp, nums[temp], n)
            # # wont be one item loop
            if temp == fast:
                return False
            # they finally meet
            if slow == fast:
                break
        return True

    def calNextIdx(self, idx, steps, n):
        return (n + idx + steps) % n


# true
a = [2, -1, 1, 2, 2]
print(Solution().circularArrayLoop(a))

# false
a = [-1, 2]
print(Solution().circularArrayLoop(a))

# false
a = [-2, 1, -1, -2, -2]
print(Solution().circularArrayLoop(a))

# true
a = [2, 1, 2, 1, 1]
print(Solution().circularArrayLoop(a))

# true
a = [2, 1, 2, 1, 3]
print(Solution().circularArrayLoop(a))

# true
a = [3, 1, 2]
print(Solution().circularArrayLoop(a))

# false
a = [2, -1, 1, -2, -2]
print(Solution().circularArrayLoop(a))

# false
a = [-1, -2, -3, -4, -5]
print(Solution().circularArrayLoop(a))

# True
a = [1, -1, 1, 3]
print(Solution().circularArrayLoop(a))

# False
a = [2, 2, 2, 2, 2, 4, 7]
print(Solution().circularArrayLoop(a))

# true
a = [-1, -1, -1]
print(Solution().circularArrayLoop(a))
