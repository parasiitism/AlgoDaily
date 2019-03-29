import bisect
import sys

# try bisect
# bisect_left: lower bound
# bisect_right: upper bound
print("------------ start try bisect ------------")

a = [3, 5, 7, 7, 7, 9, 11]
print(bisect.bisect_left(a, 7))
print(bisect.bisect_right(a, 7))

a = [10, 20, 30, 40]
print(bisect.bisect_left(a, 30))
print(bisect.bisect_right(a, 30))

print(bisect.bisect(a, 18))

print("------------ end try bisect ------------")


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int

        1st approach: binary search
        - for each house, binary search to look for the nearest heater(so we should sort heaters first)
        - the max diff is the result

        Time    O(nlogn+mlogn) n:heaters, m: houses
        Space   O(1)
        656 ms, faster than 5.11%
        """
        heaters = sorted(heaters)
        res = -1
        for house in houses:
            idx = self.bSearchNearest(heaters, house)
            diff = abs(house - heaters[idx])
            res = max(res, diff)
        return res

    def bSearchNearest(self, nums, target):
        """
        e.g. a = [10, 20, 30, 40]
        print(Solution().bSearchNearest(a, 9)) <- 0
        print(Solution().bSearchNearest(a, 10)) <- 0
        print(Solution().bSearchNearest(a, 13)) <- 0
        print(Solution().bSearchNearest(a, 21)) <- 1
        print(Solution().bSearchNearest(a, 26)) <- 2
        print(Solution().bSearchNearest(a, 34)) <- 2
        print(Solution().bSearchNearest(a, 35)) <- 3
        print(Solution().bSearchNearest(a, 41)) <- 3
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)/2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # compare and find the idx of the nearest item
        if right < 0:
            return 0
        if left > len(nums)-1:
            return len(nums)-1
        if abs(target - nums[right]) < abs(target - nums[left]):
            return right
        return left


print("------------ start try bSearchNearest ------------")
a = [10, 20, 30, 40]
print(Solution().bSearchNearest(a, 9))
print(Solution().bSearchNearest(a, 10))
print(Solution().bSearchNearest(a, 13))
print(Solution().bSearchNearest(a, 21))
print(Solution().bSearchNearest(a, 26))
print(Solution().bSearchNearest(a, 34))
print(Solution().bSearchNearest(a, 35))
print(Solution().bSearchNearest(a, 41))
print("------------ end try bSearchNearest ------------")

a = [1, 2, 3]
b = [2]
print(Solution().findRadius(a, b))

a = [1, 2, 3, 4]
b = [1, 4]
print(Solution().findRadius(a, b))


a = [10, 20, 30, 40]
b = [12, 23, 38]
print(Solution().findRadius(a, b))

a = [282475249, 622650073, 984943658, 144108930,
     470211272, 101027544, 457850878, 458777923]
b = [823564440, 115438165, 784484492, 74243042, 114807987,
     137522503, 441282327, 16531729, 823378840, 143542612]
print(Solution().findRadius(a, b))

a = [282475249, 622650073, 984943658, 144108930,
     470211272, 101027544, 457850878, 458777923]
b = [100000000, 200000000, 784484492, 300000000,
     400000000, 441282327, 800000000, 900000000]
print(Solution().findRadius(a, b))
