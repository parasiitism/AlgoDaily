"""
    1st approach: brute force
    Time    O(n)
    Space   O(n)
    LTE
"""


class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        zigzag = [1]
        q = [1]
        layerIdx = 1
        while q[-1] <= label:
            arr = []
            n = len(q)
            for i in range(n):
                head = q.pop(0)
                left = head * 2
                right = head * 2 + 1
                arr.append(left)
                arr.append(right)
            q += arr
            if layerIdx % 2 == 0:
                zigzag += arr
            else:
                zigzag += arr[::-1]
            layerIdx += 1
        # print(len(zigzag))
        labelIdx = len(zigzag)-1
        while zigzag[labelIdx] != label:
            labelIdx -= 1
        # print(labelIdx)
        res = []
        while labelIdx > 0:
            # print(labelIdx)
            res.append(zigzag[labelIdx])
            labelIdx = (labelIdx-1)//2

        return [1]+res[::-1]


"""
    learned from others: math

    ref:
    - https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/discuss/324011/Python-O(logn)-time-and-space-with-readable-code-and-step-by-step-explanation
    - https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/discuss/323676/python-simple-solution-with-explanation

    Time    O(logn)
    Space   O(n)
    16 ms, faster than 73.11%
"""


class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        res = []
        while label:
            res.append(label)
            label /= 2
        res = res[::-1]
        for i in range(len(res)-2, 0, -2):
            res[i] = 2**(i+1) - 1 + 2**i - res[i]
        return res


s = Solution()

print(s.pathInZigZagTree(14))
print(s.pathInZigZagTree(26))
