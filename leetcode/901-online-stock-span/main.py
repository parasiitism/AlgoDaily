"""
    1st approach: stack
    - similar to minstack
    
    e.g. [100, 80, 60, 70, 60, 75, 85]
    when next(100), stack = [100:1
    when next(80),  stack = [100:1, 80: 1
    when next(60),  stack = [100:1, 80: 1, 60: 1
    when next(70),  stack = [100:1, 80: 1, 70: 2
    when next(60),  stack = [100:1, 80: 1, 70: 2, 60: 1
    when next(75),  stack = [100:1, 80: 1, 75: 4
    when next(85),  stack = [100:1, 85: 6

    Time of next()      O(n) at worse but average O(1) because stock prices flutuate
    Space               O(n)
    440 ms, faster than 98.45%
"""


class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            pop = self.stack.pop()
            weight += pop[1]
        self.stack.append((price, weight))
        return weight
