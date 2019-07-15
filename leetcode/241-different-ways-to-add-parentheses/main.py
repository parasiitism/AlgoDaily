"""
    1st approach: recursion
    - similar to wordbreak2
    - slice a string into 2 parts when there is a +-*, compute each part recursively
    - in the recursive function, the base case is when string == one number
    
    e.g. 2*3-4*5
    on the highest level, f(2*3-4*5), can be splitted into
    1. f(2) * f(3-4*5) = 2 * {-17, -5}
    2. f(2*3) - f(4*5) = ...
    3. f(2*3-4) * f(5) = {-10, 10}

    f(3-4*5) can be splitted into
    1. f(3) - f(4*5)
    2. f(3-4) * f(5)

    f(2*3-4) can be splitted into
    1. f(2) * f(3-4)
    2. f(2*3) - f(4)

    one sign:
    f(4*5) = f(4) * f(5) = 20
    f(3-4) = f(3) - f(4) = -1
    f(2*3) = f(2) * f(3) = 6

    base case:
    f(4) = 4...etc

    So imagine if both size have different possibilities
    e.g. { a, b, c } * { d, e }
    the final result wil be { ad, ae, bd, be, cd, ce }

    ref:
    - https://www.youtube.com/watch?v=gxYV8eZY0eQ
    - ./idea.jpg

    Time    O(2^n) n is the number of operators in the input
    Space   O(2^n) recursion tree
    24 ms, faster than 73.46%
"""


class Solution(object):
    def diffWaysToCompute(self, s):
        """
        :type input: str
        :rtype: List[int]
        """
        result = []
        for i in range(len(s)):
            cur = s[i]
            if cur == '+' or cur == '-' or cur == '*':
                left = self.diffWaysToCompute(s[:i])
                right = self.diffWaysToCompute(s[i+1:])
                for a in left:
                    for b in right:
                        if cur == '+':
                            result.append(a+b)
                        elif cur == '-':
                            result.append(a-b)
                        elif cur == '*':
                            result.append(a*b)
        if len(result) == 0:
            result.append(int(s))
        return result


s = Solution()

a = "2-1-1"
print(s.diffWaysToCompute(a))

a = '2*3-4*5'
print(s.diffWaysToCompute(a))

a = '3+4*5*3-4*5'
print(s.diffWaysToCompute(a))
