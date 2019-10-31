"""
    1st: hashtable

    Time of createPath()    O(s)
    Time of get()           O(1)
    264 ms, faster than 73.58%
"""


class FileSystem(object):

    def __init__(self):
        self.ht = {
            '': -1
        }

    def createPath(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        if path in self.ht:
            return False
        else:
            for i in range(len(path)-1, -1, -1):
                if path[i] == '/':
                    break
            parent = path[:i]
            if parent in self.ht:
                self.ht[path] = value
                return True
            return False

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        if path in self.ht:
            return self.ht[path]
        return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
