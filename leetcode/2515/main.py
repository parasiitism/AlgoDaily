"""
    array: iterate forward and backward

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        AB = words+words

        i = startIndex
        diff_right = -1
        while i < len(AB):
            w = AB[i]
            if w == target:
                diff_right = i - startIndex
                break
            i += 1

        i = startIndex + len(words)
        diff_left = -1
        while i >= 0:
            w = AB[i]
            if w == target:
                diff_left = startIndex + len(words) - i
                break
            i -= 1

        return min(diff_right, diff_left)
