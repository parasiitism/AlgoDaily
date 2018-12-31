# recursive dfs
# e.g. [1,2,3]
#    1          2         3
# 2,3 3,2   1,3  3,1    1,2 2,1
#
# therefore, the crux is dfs(nums[:i]+arr[i+1:], prefix+[nums[i]])
# beats 32.64%


class Solution(object):

    def __init__(self):
        self.result = []

    def permute(self, nums):
        self.dfs(nums, [])
        return self.result

    def dfs(self, nums, prefix):
        if len(nums) == 0:
            self.result.append(prefix)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], prefix + [nums[i]])


# s = Solution()
# print(s.permute([1, 2, 3]))

# iterative insertion
# e.g. [1,2,3]
#   1
#  ^ ^
#  2 2
#
#   2,1         1,2
#  ^ ^ ^       ^ ^ ^
#  3 3 3       3 3 3
# beats 32.64%


def permute1(nums):
    perms = [[]]
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(perm)+1):
                new_perms.append(perm[:i] + [n] + perm[i:])
        perms = new_perms
    return perms


print(permute1([1, 2, 3]))
