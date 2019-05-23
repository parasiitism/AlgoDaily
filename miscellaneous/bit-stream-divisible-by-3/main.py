"""
    You receive a bit stream (0 and 1). 
    Continuously receive a  stream of bit, 
    each time you have to determine whether the current value is divisibility by 3 and print True or False
    For example: 
    1st: 1 -> 1 -> False (1) 
    2nd: 1 -> 11 -> True (3) 
    3rd: 0 -> 110 -> True (6) 
    4th: 1 -> 1101 -> False (7)
    ...
"""

"""
    1st approach: compare bits at odd and even places

    Problem: if the stream is big, it overflows
"""


class IsMultipleOf3(object):
    def __init__(self):
        self.isEven = True
        self.oddSetCount = 0
        self.evenSetCount = 0

    def inputAndCheck(self, b):
        if b == 1:
            if self.isEven:
                self.evenSetCount += 1
            else:
                self.oddSetCount += 1
        # avoid leading zeros
        if self.evenSetCount > 0:
            self.isEven = not self.isEven
        return (self.oddSetCount - self.evenSetCount) % 3 == 0


im3 = IsMultipleOf3()
print(im3.inputAndCheck(0))
print(im3.inputAndCheck(0))
print(im3.inputAndCheck(0))
print(im3.inputAndCheck(1))  # 1         -> 1
print(im3.inputAndCheck(1))  # 11        -> 3
print(im3.inputAndCheck(0))  # 110       -> 6
print(im3.inputAndCheck(1))  # 1101      -> 13
print(im3.inputAndCheck(0))  # 11010     -> 26
print(im3.inputAndCheck(1))  # 110101    -> 53
print(im3.inputAndCheck(0))  # 1101010   -> 106
print(im3.inputAndCheck(1))  # 11010101  -> 213

print("-----")

"""
    2nd approach: 
    - in each round, bit shift then add a bit
    - only save the reminder(%3) to proceed in the next round
"""


class IsMultipleOf3(object):
    def __init__(self):
        self.num = 0

    def inputAndCheck(self, b):
        num = (self.num << 1) + b
        self.num = num % 3
        return self.num == 0


im3 = IsMultipleOf3()
print(im3.inputAndCheck(0))
print(im3.inputAndCheck(0))
print(im3.inputAndCheck(0))
print(im3.inputAndCheck(1))  # 1         -> 1
print(im3.inputAndCheck(1))  # 11        -> 3
print(im3.inputAndCheck(0))  # 110       -> 6
print(im3.inputAndCheck(1))  # 1101      -> 13
print(im3.inputAndCheck(0))  # 11010     -> 26
print(im3.inputAndCheck(1))  # 110101    -> 53
print(im3.inputAndCheck(0))  # 1101010   -> 106
print(im3.inputAndCheck(1))  # 11010101  -> 213
