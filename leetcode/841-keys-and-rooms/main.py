"""
    1st approach: iterative dfs

    Time    O(n)
    Space   O(n)
    68 ms, faster than 24.53%
"""


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if len(rooms) == 0:
            return False
        hs = set()
        hs.add(0)
        stack = []
        for key in rooms[0]:
            stack.append(key)
        while len(stack) > 0:
            pop = stack.pop()
            hs.add(pop)
            for key in rooms[pop]:
                if key in hs:
                    continue
                stack.append(key)

        for i in range(len(rooms)):
            if i not in hs:
                return False

        return True


"""
    2nd approach: recursive dfs

    Time    O(n)
    Space   O(n)
    52 ms, faster than 28.16%
"""


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if len(rooms) == 0:
            return False
        hs = set()
        self.dfs(0, rooms, hs)
        # check each room
        for i in range(len(rooms)):
            if i not in hs:
                return False

        return True

    def dfs(self, num, rooms, hs):
        if num in hs:
            return
        hs.add(num)
        keys = rooms[num]
        for key in keys:
            self.dfs(key, rooms, hs)
