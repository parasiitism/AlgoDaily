"""
    1st: array + math

    Time    O(N)
    Space   O(N)
    1023 ms, faster than 5.21%
"""


class ATM:

    def __init__(self):
        self.inventory = 5 * [0]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.inventory[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        notes = [20, 50, 100, 200, 500]
        _inventory = self.inventory[:]
        res = [0, 0, 0, 0, 0]
        for i in range(4, -1, -1):
            _cnt = amount // notes[i]
            cnt = min(_inventory[i], _cnt)
            res[i] += cnt
            _inventory[i] -= cnt
            amount -= cnt * notes[i]
        if amount > 0:
            return [-1]
        self.inventory = _inventory
        return res


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
