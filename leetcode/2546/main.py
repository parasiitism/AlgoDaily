"""
    observation

    When we do OR and XOR, there are only 4 cases
    (0, 0) -> (0, 0)
    (1, 0) -> (1, 1)
    (0, 1) -> (1, 1)
    (1, 1) -> (1, 0)

    Observation:
    - Two 0s stay 0s.
    - If we have at least one 1, we can make (1, 1)
    - If we have two 1s, we can make any 1 to 0.

    So,
    - All 0 string can not change.
    - Any other strings can transform to any 0 or 1

    To conclude, we just need to check if there is at least any 1 in both strings

    ref:
    - https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/solutions/3083831/java-c-python-1-line-check-1/?orderBy=most_votes

    Time    O(d)
    Space   O(1)
"""


class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return ('1' in s) == ('1' in target)
