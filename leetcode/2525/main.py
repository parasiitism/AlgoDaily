"""
    if-else logic

    Time    O(1)
    Space   O(1)
"""


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        is_bulky = length * width * height >= 10**9 \
            or any([length >= 10**4, width >= 10**4, height >= 10**4])
        is_heavy = mass >= 100
        if is_bulky and is_heavy:
            return 'Both'
        elif is_bulky:
            return 'Bulky'
        elif is_heavy:
            return 'Heavy'
        return 'Neither'
