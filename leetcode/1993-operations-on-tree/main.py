"""
    1st: BFS
    - just implement description

    Time    O(N)
    Space   O(N)
    1672 ms, faster than 75.00%
"""


class LockingTree:

    def __init__(self, parent: List[int]):
        n = len(parent)
        self.parent = parent
        self.locked = n * [None]
        self.graph = {}
        for i in range(n):
            self.graph[i] = []
        for i in range(1, n):
            self.graph[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num]:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False
        self.locked[num] = None
        return True

    def upgrade(self, num: int, user: int) -> bool:
        # find the eldest ancestors, like finding the root in Union Find
        temp = num
        while temp != -1:
            if self.locked[temp]:
                return False
            temp = self.parent[temp]
        # BFS the descendants
        unlockCount = 0
        q = [num]
        while len(q) > 0:
            node = q.pop(0)
            if self.locked[node]:
                self.locked[node] = None
                unlockCount += 1
            for child in self.graph[node]:
                q.append(child)
        # only lock the current node if unlockCount > 0 as told
        if unlockCount > 0:
            self.locked[num] = user
        return unlockCount > 0


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
