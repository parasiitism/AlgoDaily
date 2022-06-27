class Solution:
    def greatestLetter(self, s: str) -> str:
        uppers = 26 * [0]
        lowers = 26 * [0]
        for c in s:
            upper_idx = ord(c) - ord('A')
            lower_idx = ord(c) - ord('a')
            if 0 <= upper_idx < 26:
                uppers[upper_idx] += 1
            if 0 <= lower_idx < 26:
                lowers[lower_idx] += 1
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(25, -1, -1):
            if uppers[i] > 0 and lowers[i] > 0:
                return alphabet[i]
        return ""
