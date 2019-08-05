class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type text: str
        :rtype: str
        """
        count = 26 * [0]
        for c in s:
            idx = ord(c) - ord('a')
            count[idx] += 1
        stack = []
        used = 26 * [False]
        for c in s:
            idx = ord(c) - ord('a')
            count[idx] -= 1
            if used[idx] == True:
                continue
            while len(stack) > 0 and stack[-1] > c and count[ord(stack[-1]) - ord('a')] > 0:
                pop = stack.pop()
                used[ord(pop) - ord('a')] = False
            stack.append(c)
            used[idx] = True
        return ''.join(stack)
