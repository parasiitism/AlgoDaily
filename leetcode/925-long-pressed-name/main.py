"""
    1st approach: 2 pointers
    - count the consecutive duplicate characters(CDC) of the 'name'
    - count the consecutive duplicate characters(CDC) of the 'typed'
    - compare and see if CDC of 'name' > CDC of 'typed', if yes return False
    - else iterate forward
    - after all, 2 pointers should point to the end of corresponding string

    Time    O(min(M,N))
    Space   O(1)
    20 ms, faster than 66.38%
"""


class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if len(name) == 0 and len(typed) == 0:
            return True
        elif len(name) == 0 or len(typed) == 0:
            return False
        p1, p2 = 0, 0
        cur1, cur2 = name[0], typed[0]
        count1, count2 = 1, 1
        while p1 < len(name) and p2 < len(typed):

            while p1+1 < len(name) and name[p1+1] == cur1:
                p1 += 1
                count1 += 1

            if cur1 != cur2:
                return False

            while p2+1 < len(typed) and typed[p2+1] == cur2:
                p2 += 1
                count2 += 1

            if count1 > count2:
                return False

            p1 += 1
            p2 += 1
            if p1 == len(name) or p2 == len(typed):
                break
            cur1 = name[p1]
            cur2 = typed[p2]
            count1 = 1
            count2 = 1
        return p1 == len(name) and p2 == len(typed)
