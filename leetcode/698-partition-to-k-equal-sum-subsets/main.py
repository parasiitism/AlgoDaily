class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        agg = sum(nums)
        target = agg / float(k)
        if target.is_integer() == False:
            return False
        target = int(target)

        self.res = 0
        used = set()
        for i in range(len(nums)):
            if i not in used:
                # print('i', i)
                num = nums[i]
                used.add(i)
                if self.dfs(nums, target, [num], num, used) == False:
                    used.remove(i)

        return self.res == k

    def dfs(self, cands, target, arr, agg, used):
        if agg == target:
            self.res += 1
            print(arr)
            return True
        elif agg > target:
            return False
        for i in range(len(cands)):
            if i not in used:
                cand = cands[i]
                used.add(i)
                if self.dfs(cands, target, arr+[cand], agg+cand, used):
                    return True
                used.remove(i)
        return False


s = Solution()

a = [4, 3, 2, 3, 5, 2, 1]
b = 4
print(s.canPartitionKSubsets(a, 4))

a = [2, 2, 2, 2, 3, 4, 5]
b = 4
print(s.canPartitionKSubsets(a, 4))

a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
b = 5
print(s.canPartitionKSubsets(a, b))

# very good test case
a = [10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6]
b = 3
print(s.canPartitionKSubsets(a, b))
