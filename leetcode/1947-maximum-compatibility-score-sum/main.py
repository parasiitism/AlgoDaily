"""
    1st: backtracking + hashtable
    - use backtracking(recursion) to select a mentor
    - memorize the selected mentors for avoiding duplicate selection
    - in every recursion, use selected mentors as a key to cache the max score from its recursion leaves 
    
    Time    O(M^M * N) for every student, there are at most M mentors to choose 
    Space   O(M)
    100 ms, faster than 83.57%
"""


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        M = len(students)
        N = len(students[0])
        selected = M * [False]
        cache = {}

        def dfs(idx):
            if idx == M:
                return 0
            key = tuple(selected)
            if key in cache:
                return cache[key]
            scoreFromBack = 0
            for i in range(M):
                if selected[i]:
                    continue
                selected[i] = True
                score = 0
                for j in range(N):
                    if students[idx][j] == mentors[i][j]:
                        score += 1
                scoreFromBack = max(scoreFromBack, dfs(idx+1) + score)
                selected[i] = False
            cache[key] = scoreFromBack
            return scoreFromBack

        return dfs(0)
