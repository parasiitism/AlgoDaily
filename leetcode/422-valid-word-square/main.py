"""
    1st approach: use error

    Time    O(n)
    Space   O(1)
    48 ms, faster than 81.87% 
"""


class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        try:
            for i in range(len(words)):
                for j in range(len(words[i])):
                    if words[i][j] != words[j][i]:
                        return False
            return True
        except IndexError:
            return False


a = [
    "abcd",
    "bnrt",
    "crmy",
    "dtye"
]
print(Solution().validWordSquare(a))

a = ["ball", "asee", "lett", "le"]
print(Solution().validWordSquare(a))

a = ["ball", "asee", "let", "let"]
print(Solution().validWordSquare(a))

print("----")

"""
    2nd approach: use error

    Time    O(n)
    Space   O(1)
    76 ms, faster than 26.94%
"""


class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j >= len(words):
                    # longer: no such row
                    print("longer")
                    return False
                elif i >= len(words[j]):
                    # shorter: no such col
                    print("shorter")
                    return False
                elif words[i][j] != words[j][i]:
                    # not equal
                    return False
        return True


a = [
    "abcd",
    "bnrt",
    "crmy",
    "dtye"
]
print(Solution().validWordSquare(a))

# shorter: if i >= len(words[j]):
a = [
    "ball",
    "asee",
    "lett",
    "le",
]
print(Solution().validWordSquare(a))

# shorter: if i >= len(words[j]):
a = [
    "ball",
    "asee",
    "let",
    "let",
]
print(Solution().validWordSquare(a))

# shorter: if j >= len(words):
a = [
    "ball",
    "asee",
    "lett",
    "lett",
    "a",
]
print(Solution().validWordSquare(a))

# longer: if i >= len(words[j]):
a = [
    "ball",
    "asee",
    "letta",
    "lett",
]
print(Solution().validWordSquare(a))
