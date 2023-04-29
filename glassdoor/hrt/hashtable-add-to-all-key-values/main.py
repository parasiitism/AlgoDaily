"""
    Create a new hashtable that add value to all the keys and values. 
    At the end, find the sum of all get() operations
"""


class NewHashtable:
    def __init__(self):
        self.keyOffset = 0
        self.valueOffset = 0
        self.ht = {}

    def insert(self, key, val):
        self.ht[key - self.keyOffset] = val - self.valueOffset

    def get(self, key):
        return self.ht[key - self.keyOffset] + self.valueOffset

    def addToKey(self, toAdd):
        self.keyOffset += toAdd

    def addToVale(self, toAdd):
        self.valueOffset += toAdd


total = 0
nht = NewHashtable()
nht.insert(1, 2)
nht.insert(2, 3)
nht.addToVale(2)
nht.addToKey(1)
# print(nht.get(3))
total += nht.get(3)
print(total)

print("----")

total = 0
nht = NewHashtable()
nht.insert(1, 2)
nht.addToVale(2)
# print(nht.get(1))
total += nht.get(1)
nht.insert(2, 3)
nht.addToKey(1)
nht.addToVale(-1)
# print(nht.get(3))
total += nht.get(3)
print(total)
