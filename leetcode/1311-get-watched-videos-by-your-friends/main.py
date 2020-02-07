from collections import Counter
from collections import defaultdict

"""
    1st: BFS + hashtable
    1. BFS to get the friendlist on level k
    2. use hashtable to avoid duplicate such that we will get the shortest path to each friend at level k
    3. sort the hashtable by count

    Time    O(NlogN)
    Space   O(N)
    280 ms, faster than 36.62%
"""


class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, me, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        hs = set()
        friendsAtLevel = []
        q = [(me, 0)]
        while len(q) > 0:
            n = len(q)
            for _ in range(n):
                head, steps = q.pop(0)
                if head in hs:
                    continue
                hs.add(head)
                if steps == level:
                    friendsAtLevel.append(head)
                elif steps < level:
                    for x in friends[head]:
                        q.append((x, steps + 1))
        ht = defaultdict(int)
        for x in friendsAtLevel:
            videos = watchedVideos[x]
            for v in videos:
                ht[v] += 1

        counts = []
        for key in ht:
            counts.append([ht[key], key])
        counts.sort()

        return [x[1] for x in counts]


"""
    2nd: same as 1st but use Counter

    Time    O(NlogN)
    Space   O(N)
    292 ms, faster than 21.82%
"""


class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, me, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        hs = set()
        friendsAtLevel = []
        q = [(me, 0)]
        while len(q) > 0:
            n = len(q)
            for _ in range(n):
                head, steps = q.pop(0)
                if head in hs:
                    continue
                hs.add(head)
                if steps == level:
                    friendsAtLevel.append(head)
                elif steps < level:
                    for x in friends[head]:
                        q.append((x, steps + 1))

        temp = []
        for x in friendsAtLevel:
            temp += watchedVideos[x]
        ht = Counter(temp)

        counts = []
        for key in ht:
            counts.append([ht[key], key])
        counts.sort()

        return [x[1] for x in counts]
