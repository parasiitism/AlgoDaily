"""
  questions to ask:
  - will call next(), peek() after hasNext()? maybe
  - what is the definition/structure of the iterator?
"""

# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.buffer = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.it.hasNext():
            if self.buffer == None:
                x = self.it.next()
                self.buffer = x
                return x
            return self.buffer
        return self.buffer

    def next(self):
        """
        :rtype: int
        """
        if self.buffer != None:
            temp = self.buffer
            self.buffer = None
            return temp
        if self.it.hasNext():
            return self.it.next()
        return self.buffer

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.buffer != None:
            return True
        return self.it.hasNext()
