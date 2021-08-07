"""
    1st: recursion
    - similar idea: leetcode 698
    - learned from others
    - the main idea is try every possbility wisely

    There are several tricks:
    1. only care about the smaller sums
    2. if 2 workers have spent the same time, i.g. spends[i] = 5, spends[j] = 5, 
        there is no difference for them to work on a task which spends 6, i.e. spends[i] = 5+6=11, spends[j] = 5+6=11
        therefore, we can just compute once
    3. 

    Time    O(k^N) worst, bcos for every task, there are at most k workers to work on
    Space   O(k^N) 
    584 ms, faster than 32.35%
"""


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)

        spends = k * [0]  # time spent of every worker
        self.res = 2**32

        def dfs(taskId):
            if taskId == n:
                self.res = min(self.res, max(spends))
                return

            seen = set()
            for i in range(k):

                # 1
                if spends[i] + jobs[taskId] >= self.res:
                    continue

                # 2
                if spends[i] in seen:
                    continue
                seen.add(spends[i])

                spends[i] += jobs[taskId]
                dfs(taskId + 1)

                # dont forget to subtract the spend for the parent recursive function
                spends[i] -= jobs[taskId]

        dfs(0)
        return self.res
