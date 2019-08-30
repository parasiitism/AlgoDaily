"""
    1st: recursion + eval
    - use eval to transform array string into an array
    - do it recursively

    ref:
    - https://leetcode.com/problems/mini-parser/discuss/86060/Python-and-C%2B%2B-solutions

    Time    O(n)
    Space   O(n)
    60 ms, faster than 93.27%
"""


class Solution(object):
    def deserialize(self, s):
        def getNumber(nums):
            if isinstance(nums, int):
                return NestedInteger(nums)
            lst = NestedInteger()
            for num in nums:
                lst.add(getNumber(num))
            return lst
        return getNumber(eval(s))


"""
    2nd: recursion + queue
    - transform the input into a queue
    - there are 2 cases when we dequeue the queue
        - the upcomming string(before any , [) is a number
        - the upcomming string starts with [
    - decompose the string recursively

    ref:
    - https://leetcode.com/problems/mini-parser/discuss/86060/Python-and-C%2B%2B-solutions

    Time    O(n)
    Space   O(n)
    204 ms, faster than 5.24%
"""


class Solution(object):
    def deserialize(self, s):

        def dfs():
            num = ''
            while len(q) > 0 and q[0] in '-01234567890':
                num += q.pop(0)
            if num != '':
                return NestedInteger(int(num))
            q.pop(0)
            arr = NestedInteger()
            while len(q) > 0 and q[0] != ']':
                arr.add(dfs())
                if q[0] == ',':
                    q.pop(0)
            q.pop(0)
            return arr

        q = list(s)
        return dfs()


"""
    3rd: recursion + stack
    - optimize the 2nd approach by using .pop() instead of .pop(k) with string reversal
    - transform the input into a stack
    - there are 2 cases when we dequeue the stack
        - the upcomming string(before any , [) is a number
        - the upcomming string starts with [
    - decompose the string recursively

    ref:
    - https://leetcode.com/problems/mini-parser/discuss/86060/Python-and-C%2B%2B-solutions

    Time    O(n)
    Space   O(n)
    76 ms, faster than 51.90%
"""


class Solution(object):

    def deserialize(self, s):

        def dfs():
            num = ''
            while len(stack) > 0 and stack[-1] in '-01234567890':
                num += stack.pop()
            if num != '':
                return NestedInteger(int(num))
            stack.pop()
            arr = NestedInteger()
            while len(stack) > 0 and stack[-1] != ']':
                arr.add(dfs())
                if stack[-1] == ',':
                    stack.pop()
            stack.pop()
            return arr

        stack = list(s[::-1])
        return dfs()
