from collections import *
import sys

"""
    Given a non-empty list of words, return the 2 most frequent words.
    If there is a tie, two words have the same frequency, return them by the insertion order.

    1st approach: ordered dict
    - lc692
"""


class Solution(object):
    def topKFrequent(self, words):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        m = OrderedDict()
        for word in words:
            if word not in m:
                m[word] = 1
            else:
                m[word] += 1
        occurences = {}
        largest = -sys.maxsize
        secondLargest = -sys.maxsize
        for key in m:
            occurence = m[key]
            if occurence not in occurences:

                # find largest and secondLargest
                if occurence > largest:
                    secondLargest = largest
                    largest = occurence
                elif occurence < largest and occurence > secondLargest:
                    secondLargest = occurence

                occurences[occurence] = [key]
            else:
                occurences[occurence].append(key)

        count = 0
        res = []
        arr1 = occurences[largest]
        res += arr1[:2]
        if len(res) < 2:
            arr2 = occurences[secondLargest]
            res += [arr2[0]]

        return res


a = ["love", "i", "leetcode", "i", "love", "coding"]
print(Solution().topKFrequent(a))

a = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
print(Solution().topKFrequent(a))

a = ["aaa", "aa", "a"]
print(Solution().topKFrequent(a))

print("-----")

"""
    2nd approach: hashtable + array to similate ordered dict
    - since we wont delete keys, we can just use an array to do it
"""


class Node(object):
    def __init__(self, key, count):
        self.key = key
        self.count = count


class Solution(object):
    def topKFrequent(self, words):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        m = {}
        nodes = []
        for word in words:
            if word not in m:
                m[word] = len(nodes)
                nodes.append(Node(word, 1))
            else:
                idx = m[word]
                node = nodes[idx]
                node.count += 1
        occurences = {}
        largest = -sys.maxsize
        secondLargest = -sys.maxsize
        for node in nodes:
            occurence = node.count
            if occurence not in occurences:

                # find largest and secondLargest
                if occurence > largest:
                    secondLargest = largest
                    largest = occurence
                elif occurence < largest and occurence > secondLargest:
                    secondLargest = occurence

                occurences[occurence] = [node.key]
            else:
                occurences[occurence].append(node.key)

        count = 0
        res = []
        arr1 = occurences[largest]
        res += arr1[:2]
        if len(res) < 2:
            arr2 = occurences[secondLargest]
            res += [arr2[0]]

        return res


a = ["love", "i", "leetcode", "i", "love", "coding"]
print(Solution().topKFrequent(a))

a = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
print(Solution().topKFrequent(a))

a = ["aaa", "aa", "a"]
print(Solution().topKFrequent(a))

print("-----")

"""
    followup: top k

	Time	O(nlogn * klogk)
	Space	O(n)
	44 ms, faster than 67.17%
	30may2019
"""


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        m = OrderedDict()
        for word in words:
            if word not in m:
                m[word] = 1
            else:
                m[word] += 1
        occurences = {}
        keys = []
        for key in m:
            occurence = m[key]
            if occurence not in occurences:
                keys.append(occurence)
                occurences[occurence] = [key]
            else:
                occurences[occurence].append(key)
        keys = sorted(keys, reverse=True)
        count = 0
        res = []
        for i in range(len(keys)):
            freq = keys[i]
            strings = occurences[freq]
            for s in strings:
                res.append(s)
                count += 1
                if count == k:
                    break
            if count == k:
                break
        return res


a = ["love", "i", "leetcode", "i", "love", "coding"]
b = 2
print(Solution().topKFrequent(a, b))

a = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
b = 4
print(Solution().topKFrequent(a, b))

a = ["aaa", "aa", "a"]
b = 2
print(Solution().topKFrequent(a, b))
