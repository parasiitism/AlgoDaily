"""
    learned from others
	2nd approach: hashtable + array
	- save value: index in hashtable
	- when delete, swap the target item and the last item in the array, and remove the last item
	- see ./idea_add.png and ./idea_remove.png

	Insert Time				O(1)
	Remove Time				O(1)
	GetRandom Time		O(1)
	Space							O(n) the unique keys
	92 ms, faster than 78.93%
"""
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ht = {}
        self.nums = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.ht:
            return False
        self.ht[val] = len(self.nums)
        self.nums.append(val)
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.ht:
            return False
        idx = self.ht[val]
        last = self.nums[-1]
        self.ht[last] = idx
        self.nums[idx] = last
        self.nums.pop()
        del self.ht[val]
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randint(0, len(self.nums)-1)
        return self.nums[idx]