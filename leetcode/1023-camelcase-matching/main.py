"""
    1st approach: brute force
    - iterate the queries
    - put pattern into a queue
    - iterate each character in a query
        - if there is a match, dequeue the queue
        - if there is capital letter doesnt match the queue head, return False
        - after the iteration, if there is still some characters in the queue, return False
        - else return True

    Time    O(PQ)
    Space   O(Q)
    20 ms, faster than 65.63%
"""


class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        res = []
        for query in queries:
            queue = pattern[:]
            didBreak = False
            for i in range(len(query)):
                if len(queue) > 0:
                    if query[i] == queue[0]:
                        queue = queue[1:]
                    elif 65 <= ord(query[i]) <= 90:
                        res.append(False)
                        didBreak = True
                        break
                elif 65 <= ord(query[i]) <= 90:
                    res.append(False)
                    didBreak = True
                    break
            if didBreak == False:
                if len(queue) > 0:
                    res.append(False)
                else:
                    res.append(True)
        return res
