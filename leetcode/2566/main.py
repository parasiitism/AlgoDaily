"""
    1st: greedy
    
    Time    O(10D) number of digits of num
    Space   O(1)
"""
class Solution:
    def minMaxDifference(self, num: int) -> int:
        max_num = num
        min_num = num
        for i in range(10):
            chars = [c for c in str(num)]
            x = ''
            y = ''
            for c in chars:
                if c == str(i):
                    x += '9'
                    y += '0'
                else:
                    x += c
                    y += c
            max_num = max(max_num, int(x))
            min_num = min(min_num, int(y))
        return max_num - min_num
