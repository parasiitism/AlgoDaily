"""
    1st: 2 hashtables
    - one for recording the index: number
    - one for recording the number: [idx0, idx1, idx2,...]
    
    Time of change()    O(N)
    Time of find()      O(N)
    LTE
"""


from sortedcontainers import SortedList


class NumberContainers:

    def __init__(self):
        self.mapIdx2Num = {}  # {2: 10, 1: 10, 3: 10, 5: 10}
        self.mapNumAtIndices = defaultdict(set)  # {10: {1,2,3,5}, 20}

    def change(self, index: int, number: int) -> None:
        if index in self.mapIdx2Num:
            _number = self.mapIdx2Num[index]
            self.mapNumAtIndices[_number].remove(index)
            if len(self.mapNumAtIndices[_number]) == 0:
                del self.mapNumAtIndices[_number]
        self.mapIdx2Num[index] = number
        self.mapNumAtIndices[number].add(index)

    def find(self, number: int) -> int:
        indices = self.mapNumAtIndices[number]
        if len(indices) == 0:
            return -1
        return min(indices)


"""
    2nd: optimize the 1st approach using a SortedList

    Time of change()    O(N)
    Time of find()      O(logN) average, O(N) worst
    LTE
"""


class NumberContainers:

    def __init__(self):
        self.mapIdx2Num = {}  # {2: 10, 1: 10, 3: 10, 5: 10}
        self.mapNumAtIndices = defaultdict(SortedList)  # {10: {1,2,3,5}, 20}

    def change(self, index: int, number: int) -> None:
        if index in self.mapIdx2Num:
            _number = self.mapIdx2Num[index]
            self.mapNumAtIndices[_number].discard(index)
            if len(self.mapNumAtIndices[_number]) == 0:
                del self.mapNumAtIndices[_number]
        self.mapIdx2Num[index] = number
        self.mapNumAtIndices[number].add(index)

    def find(self, number: int) -> int:
        if number in self.mapNumAtIndices:
            return self.mapNumAtIndices[number][0]
        return -1
