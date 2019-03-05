"""
    questions to ask:
    - it is sure that i can find out the endWord in wordList? no
    - will there be duplicate in wordList? might be
"""


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        1st approach: BFS + hashset to avoid loop
        - similar to leetcode 127) word ladder

        Time    O(M×N)  
            M=length of gene, in this case is 8
            N=number of genes in the bank
            Finding out all the transformations takes M iterations for each of the N genes. 
            Also, breadth first search in the worst case might go to each of the N gene.
        Space   O(n)
        16 ms, faster than 100.00%
        """
        bank = set(bank)  # avoid duplicate words
        if end not in bank:
            return -1
        # BFS
        q = []
        q.append((start, 0))
        seen = set()  # avoid revisting a seen word
        alphabets = "ATGC"
        while len(q) > 0:
            word, level = q.pop(0)
            if word == end:
                return level
            # explore at index=0 hit => ait, bit, cit....
            # explore at index=1 hit => hat, hbt, hct....
            for i in range(len(word)):
                for c in alphabets:
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in bank and newWord not in seen:
                        q.append((newWord, level + 1))
                        seen.add(newWord)
        return -1


a = "AACCGGTT"
b = "AACCGGTA"
c = ["AACCGGTA"]
print(Solution().minMutation(a, b, c))

a = "AACCGGTT"
b = "AAACGGTA"
c = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
print(Solution().minMutation(a, b, c))

a = "AAAAACCC"
b = "AACCCCCC"
c = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
print(Solution().minMutation(a, b, c))

a = "AAAAACCC"
b = "AACCCCCG"
c = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
print(Solution().minMutation(a, b, c))
