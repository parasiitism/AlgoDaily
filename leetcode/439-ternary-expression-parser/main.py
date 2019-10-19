class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        q = [x for x in expression]
        stack = []
        while len(q) > 0:
            d = q.pop(0)
            if d == '?':
                d = q.pop(0)
                stack.append(d)
            elif d == ':':
                d = q.pop(0)
                beenFalse = False
                while len(stack) > 1 and stack[-2] == 'F':
                    stack.pop()
                    beenFalse = True
                if beenFalse:
                    stack[-1] = d
                if len(stack) > 1 and stack[-2] == 'T':
                    return stack[-1]
                if beenFalse == False:
                    stack.append(d)
            else:
                stack.append(d)

        return stack[-1]


s = Solution()

a = 'T?2:3'
print(s.parseTernary(a))  # 2

a = 'F?1:T?4:5'
print(s.parseTernary(a))  # 4

a = 'T?T?T:5:3'
print(s.parseTernary(a))  # T

a = 'T?T?F:5:3'
print(s.parseTernary(a))  # F

a = 'T?F?F:5:3'
print(s.parseTernary(a))  # 5

print("-----")

a = 'F?F?F:5:3'
print(s.parseTernary(a))  # 3

a = 'F?T?F:5:3'
print(s.parseTernary(a))  # 3 ❌

a = 'T?F?T:5:3'
print(s.parseTernary(a))  # 5
