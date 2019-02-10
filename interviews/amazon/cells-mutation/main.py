"""
    Cells Mutation / Days Change

    For each cell, if the cell's neightbours(left and right) have the same value, 
    in the next day the value of the cell becomes 0, else 1 
    
    e.g.
    cells: [1, 0, 0, 0, 0, 1, 0, 0]
    day 1:
    output: [0, 1, 0, 0, 1, 0, 1, 0]
    day 2:
    output: [1, 0, 1, 1, 0, 0, 0, 1]

    Write a function to return the cells after k days of mutation.

    Questions to ask:
    - any characters other than 0 and 1?
    - empty array?
    - k < 1?
"""


def cellsMutation(cells, k):
    """
        Time    O(kn)
        Space   O(n)
    """
    if len(cells) < 1 or k < 1:
        return []
    cnt = 0
    nextCells = [0]+cells+[0]
    k = k % 8
    while cnt < k:
        temp = []
        temp.append(0)
        for i in range(1, len(nextCells)-1):
            if nextCells[i-1] == nextCells[i+1]:
                temp.append(0)
            else:
                temp.append(1)
        temp.append(0)
        nextCells = temp
        cnt += 1
    return nextCells[1:-1]


print(cellsChange([1, 0, 0, 0, 0, 1, 0, 0], 1))
print(cellsChange([1, 0, 0, 0, 0, 1, 0, 0], 2))
print(cellsChange([1, 0, 0, 0, 0, 1, 0, 0], 3))
print(cellsChange([1, 0, 0, 0, 0, 1, 0, 0], 8))
