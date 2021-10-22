"""
    1st: array? straightforward

    Time    O(1)
    Space   O(1)
    712 ms, faster than 18.18%
"""


class Bank:

    def __init__(self, balance: List[int]):
        self.n = len(balance)
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        x, y = account1-1, account2-1
        if x < 0 or x >= self.n or y < 0 or y >= self.n:
            return False
        if money > self.balance[x]:
            return False
        self.balance[x] -= money
        self.balance[y] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        x = account-1
        if x < 0 or x >= self.n:
            return False
        self.balance[x] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        x = account-1
        if x < 0 or x >= self.n:
            return False
        if money > self.balance[x]:
            return False
        self.balance[x] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
