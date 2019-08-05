"""
    1st approach: queue
    - iterate the array with 2 steps if we see 1
    - iterate the array with 1 steps if we see 0
    - check the case if last iteration at the end

    Time    O(n)
    Space   O(1)
    52 ms, faster than 9.68%
"""


class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        case = ''
        while len(bits) > 0:
            if bits[0] == 1:
                if len(bits) > 1:
                    case = '2'
                    bits = bits[2:]
                else:
                    return False
            else:
                case = '1'
                bits = bits[1:]
        return case == '1'


"""
    2nd approach:
    - iterate the array with 2 steps if we see 1
    - iterate the array with 1 steps if we see 0
    - check the case if last iteration at the end

    Time    O(n)
    Space   O(1)
    52 ms, faster than 9.68%
"""


class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                if len(bits) > 1:
                    case = '2'
                    i += 2
                else:
                    return False
            else:
                case = '1'
                i += 1
        return case == '1'
