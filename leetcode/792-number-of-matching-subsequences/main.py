"""
    questions to ask:
    - will there be duplicates in the words? yes
    - will there be empty string in words? no. yes for followup
    - will the S be empty? no. yes for followup
"""

"""
    1st approach: brute force + hashtable
    - iterate the words and check if subsequnce using the way like lc392

    Time    O(SWK)
    Space   O(W)
    2004 ms, faster than 7.80%
"""


class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        m = {}
        for word in words:
            if word not in m:
                m[word] = 1
            else:
                m[word] += 1

        count = 0
        for key in m:
            if self.isSubsequence(S, key) == True:
                count += m[key]
        return count

    def isSubsequence(self, S, word):
        if len(word) == 0:
            return True
        i = 0
        for c in S:
            if c == word[i]:
                i += 1
            if i == len(word):
                return True
        return False


"""
    2nd approach: binary search + hashtable
    
    e.g. abcdea, ["a", "bb", "acd", "ace", "acf", "acd", "aa"]

    a: [0, 5]
    b: [1]
    c: [2]
    d: [3]
    e: [4]

    for each character in word, binary search to find the index which is larget than prevIdx we found from the value(from hashtable)

    e.g. check "acda"
    find 'a', we have 0
    find 'c' for index larger than 0, we have 2
    find 'd' for index larger than 2, we have 3
    find 'a' for index larger than 3, we have 5
    
    - we sucessfully found out all the indeces from the hashtable, therefore 'acda' is a subsequnce

    e.g. check "acb"
    find 'a', we have 0
    find 'c' for index larger than 0, we have 2
    find 'b' for index larger than 2, there is no index of 'b' larger than 2
    
    - so 'acb' is not a subsequnce

    Time    O(SWlogK)
    Space   O(W)
    1472 ms, faster than 16.79%
"""


class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        # hashtable to avoid redundant calculation by recording the count of each word
        wordSet = {}
        for word in words:
            if word not in wordSet:
                wordSet[word] = 1
            else:
                wordSet[word] += 1
        # save the char: indeces as key: value
        m = {}
        for i in range(len(S)):
            c = S[i]
            if c not in m:
                m[c] = [i]
            else:
                m[c].append(i)
        # start iteration
        res = 0
        for word in wordSet:
            prev = -1
            for c in word:
                # if no such character
                if c not in m:
                    prev = -1
                    break
                # binary search to find the index which is larget than prev
                foundIdx = self.upperBsearch(m[c], prev)
                if foundIdx == len(m[c]):
                    prev = -1  # reset such that we can skip increment it to the result
                    break
                prev = m[c][foundIdx]
            # use the count of word in wordSet to avoid redundant calculation
            if prev > -1:
                res += wordSet[word]
        return res

    def upperBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)/2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return right


a = "abcdea"
b = ["a", "bb", "acd", "ace", "acf", "acda", "acd"]
print(Solution().numMatchingSubseq(a, b))
