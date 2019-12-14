from collections import defaultdict

"""
    1st: hashtable
    - group the indices by group size
    - iterate each array and put them in a same group with corresponding group size
    
    e.g. [2,1,3,3,3,2,3,3,3]
    1: [1]
    2: [0,5]
    3: [2,3,4,6,7,8]
    
    result:
    [[1],[0,5],[2,3,4],[6,7,8]]

    Time    O(N)
    Space   O(N)
    56 ms, faster than 95.72%
"""


class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        ht = defaultdict(list)
        for i in range(len(groupSizes)):
            count = groupSizes[i]
            ht[count].append(i)
        res = []
        for count in ht:
            arr = ht[count]
            for i in range(0, len(arr), count):
                res.append(arr[i:i+count])
        return res


"""
    2nd: hashtable
    - same logic as 1st but optimize it by using one less iteration
    - group the indices by group size
    - iterate each array and put them in a same group with corresponding group size
    
    e.g. [2,1,3,3,3,2,3,3,3]
    1: [1]
    2: [0,5]
    3: [2,3,4,6,7,8]
    
    result:
    [[1],[0,5],[2,3,4],[6,7,8]]

    Time    O(N)
    Space   O(N)
    52 ms, faster than 99.50%
"""


class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        ht = defaultdict(list)
        res = []
        for i in range(len(groupSizes)):
            count = groupSizes[i]
            ht[count].append(i)
            if len(ht[count]) == count:
                res.append(ht[count])
                ht[count] = []
        return res
