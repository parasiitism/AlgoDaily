"""
    1st approach: stack
    - a stack stores (num, left, right) typed (int, bool, bool) to indicate one node
    - on one node, if both of its children are filled
        1. pop this node from stack
        2. fill its parent's child
        3. repeat until both children are not filled
    - at the end, if no more items and len(stack) == 0, valid

    e.g. [9,3,4,#,#,1,#,#,2,#,6,#,#]
    
    put 9,3,4
    (4,false, false)
    (3,false, false)
    (9,false, false)

    put #,#
    (4,true, true)
    (3,false, false)
    (9,false, false)
        becomes
    (3,true, false)
    (9,false, false)

    put 1
    (1,false, false)
    (3,true, false)
    (9,false, false)

    put #,#
    (1,true, true)
    (3,true, false)
    (9,false, false)
        becomes
    (3,true, true)
    (9,false, false)
        becomes
    (9,true, false)

    put 2
    (2,false, false)
    (9,true, false)

    put #
    (2,true, false)
    (9,true, false)

    put 6
    (6,false, false)
    (2,true, false)
    (9,true, false)

    put #,#
    (6,true, true)
    (2,true, false)
    (9,true, false)
        becomes
    (2,true, true)
    (9,true, false)
        becomes
    (9,true, true)
        becomes
    [ empty stack ]

    Time    O(n)
    Space   O(n)
    32 ms, faster than 41.13%
"""


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        if len(nodes) == 1 and nodes[0] == '#':
            return True
        stack = []
        while len(nodes) > 0:
            pop = nodes.pop(0)
            if pop != '#':
                stack.append([pop, False, False])
            else:
                if len(stack) > 0 and stack[-1][1] == False:
                    stack[-1][1] = True
                elif len(stack) > 0 and stack[-1][2] == False:
                    stack[-1][2] = True
                    while len(stack) > 0 and stack[-1][2] == True:
                        stack.pop()
                        if len(stack) == 0:
                            break
                        if stack[-1][1] == False:
                            stack[-1][1] = True
                        elif stack[-1][2] == False:
                            stack[-1][2] = True
            if len(stack) == 0:
                break
        return len(nodes) == 0 and len(stack) == 0


s = Solution()

a = "9,3,4,#,#,1,#,#,2,#,6,#,#"
print(s.isValidSerialization(a))

a = "9,3,4,#,#,1,#,#,2,#,6,#"
print(s.isValidSerialization(a))

a = "9,3,4,#,#,1,#,#,2,#,6,#,#,#"
print(s.isValidSerialization(a))

a = "9,3,4,#,#,1,#,#,#,2,#,6,#,#"
print(s.isValidSerialization(a))

a = "1"
print(s.isValidSerialization(a))

a = "1,#"
print(s.isValidSerialization(a))

a = "1,#,#"
print(s.isValidSerialization(a))

a = "9,#,#,1"
print(s.isValidSerialization(a))

a = '#'
print(s.isValidSerialization(a))

a = '#,1'
print(s.isValidSerialization(a))
