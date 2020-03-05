from typing import List

"""
    1st: prefix sum + hashtable
    e.g. s = abcda
    find the occurence of each letter when we traverse the string
    s at idx 0: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    s at idx 1: [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    s at idx 2: [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    s at idx 3: [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    s at idx 4: [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    e.g.1 queries = [1, 3], 
    occurences[3] - occurence[0] = [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    e.g.2 queries = [0, 3],
    occurences[3] = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    To determine the number of arbitory characters we need to make a substring Palindrome, 
    We can see how many odd-occurence characters.
    
    case1 even odd-occurence: if 10 odds, it means we can add 5 arbitary characters to make the substring Palindrome
    case2 odd odd-occurence:  if 9 odds, it means we can add 4 arbitary characters to make the substring Palindrome

    Time    O(26N)
    Space   O(26N)
    2296 ms, faster than 60.70%
"""


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        occurences = []
        for i in range(len(s)):
            c = s[i]
            idx = ord(c) - ord('a')
            temp = 26 * [0]
            if i > 0:
                temp = occurences[-1][:]
            temp[idx] += 1
            occurences.append(temp)

        res = []
        for left, right, k in queries:
            # matrix subtraction: [3, 4, 5] - [1, 1, 1] = [2, 3, 4]
            subStrOccurences = occurences[right][:]
            if left - 1 >= 0:
                for i in range(26):
                    subStrOccurences[i] -= occurences[left-1][i]
            # count number of odds within the substring
            numberOfOdds = 0
            for count in subStrOccurences:
                numberOfOdds += count % 2
            res.append(numberOfOdds <= 1 or numberOfOdds//2 <= k)
        return res


s = Solution()

# [true,false,false,true,true]
a = "abcda"
b = [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]
print(s.canMakePaliQueries(a, b))
