import random


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.m:
            self.m[val] += 1
            return False
        self.m[val] = 1
        return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.m:
            self.m[val] -= 1
            if self.m[val] == 0:
                del self.m[val]
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        arr = []
        for key in self.m:
            temp = [key]*self.m[key]
            arr += temp
        r = random.randint(0, len(arr)-1)
        return arr[r]


# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
print(obj.insert(1))
print(obj.insert(1))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.remove(1))
print(obj.remove(1))
print(obj.remove(1))
print(obj.m)
print(obj.getRandom())
