import copy
"""
    1st: hashtbale
        
    Time O(mn)
    Space O(mn)
    972 ms, faster than 11.33%     
"""


class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.m = []
        self.m.append({})

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        top = self.m[-1]
        top[index] = val

    def snap(self):
        """
        :rtype: int
        """
        top = self.m[-1]
        clone = copy.deepcopy(top)
        self.m.append(clone)
        return len(self.m)-2

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        ht = self.m[snap_id]
        if index in ht:
            return ht[index]
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
