"""
    hashtable

    Time    O(1)
    Space   O(1)
    1101 ms, faster than 100.00%
"""


class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.ht = {}
        for name in names:
            self.ht[name] = {}

    def insertRow(self, name: str, row: List[str]) -> None:
        row_id = len(self.ht[name])
        self.ht[name][row_id] = row

    def deleteRow(self, name: str, rowId: int) -> None:
        # we don't really have to remove it actually, cos we need to remain the rowId
        rowId -= 1
        self.ht[name][rowId] = None

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        rowId -= 1
        columnId -= 1
        return self.ht[name][rowId][columnId]


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)
