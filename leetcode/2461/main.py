"""
    2 hashtables
    - 1 for frequency of each element
    - 1 for count of each frequency

    Time    O(N)
    Space   O(N)
    3923 ms, faster than 50.00%
"""


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        window_sum = 0
        ctr = Counter()
        self.freq_cnts = {}
        res = 0
        for i in range(n):
            x = nums[i]
            window_sum += x

            self.del_freq_cnts(ctr[x])
            ctr[x] += 1
            self.add_freq_cnts(ctr[x])

            if i >= k:
                y = nums[i-k]
                window_sum -= y

                self.del_freq_cnts(ctr[y])
                ctr[y] -= 1
                if ctr[y] == 0:
                    del ctr[y]
                self.add_freq_cnts(ctr[y])

            # check distinct
            if 1 in self.freq_cnts and self.freq_cnts[1] == k:
                res = max(res, window_sum)
        return res

    def add_freq_cnts(self, cnt):
        if cnt == 0:
            return
        if cnt not in self.freq_cnts:
            self.freq_cnts[cnt] = 0
        self.freq_cnts[cnt] += 1

    def del_freq_cnts(self, cnt):
        if cnt not in self.freq_cnts and cnt == 0:
            return
        self.freq_cnts[cnt] -= 1
        if self.freq_cnts[cnt] <= 0:
            del self.freq_cnts[cnt]
