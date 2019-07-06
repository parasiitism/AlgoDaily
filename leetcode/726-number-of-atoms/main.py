from collections import *

"""
    basic, no '(' and ')'
"""


class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        q = []
        for c in formula:
            q.append(c)
        return self.recur(q)

    def recur(self, q):
        num = 0
        cur = ''
        ht = defaultdict(int)
        while len(q) > 0:
            c = q.pop(0)
            if c.isdigit():
                num = num*10+int(c)
            elif 65 <= ord(c) <= 90:
                if len(cur) > 0:
                    ht[cur] += max(num, 1)
                    num = 0
                cur = c
            elif 97 <= ord(c) <= 122:
                cur += c
        if len(cur) > 0:
            ht[cur] += max(num, 1)
            num = 0
        return ht


a = 'H2O'
print(Solution().countOfAtoms(a))

a = 'HOH'
print(Solution().countOfAtoms(a))

a = 'HHO'
print(Solution().countOfAtoms(a))

a = 'H1HO'
print(Solution().countOfAtoms(a))

a = 'H2HO'
print(Solution().countOfAtoms(a))

a = 'MgAO2HC3'
print(Solution().countOfAtoms(a))

print("-----")

"""
    with '(' and ')'

    1st approach: the basic idea is to use recursion
    - similar to lc772
    - whenever we see a '(', we go into a recursion and calculate the elements
    - whenever we see a ')', we exit the recursion and return the elements' count to its parent

    for a single element, there are 2 possibilitis
    - ...MgO...
    - ...Mg(...
    in the above cases, we should put the Mg in hashtable

    for every ), there are 3 possibilitis
    - ...OH)2...
    - ...OH)A...
    - ...OH)(...
    so we need to add the characters count in the above 3 cases

    Time    O(n^2) O(n): deqeue, inner O(n) because we need to deal with the elements from recursion 
    Space   O(n) recursion tree, hashtable
    16 ms, faster than 92.83%
"""


class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        # put all the characters into a queue such that we can pop()
        q = []
        for c in formula:
            q.append(c)
        # get all the elements count
        ht = self.recur(q)
        # construct the result by sorting the elements alphabetically
        arr = []
        for key in ht:
            arr.append((key, ht[key]))
        arr = sorted(arr, key=lambda x: x[0])
        res = ''
        for a, b in arr:
            if b > 1:
                res += a+str(b)
            else:
                res += a
        return res

    def recur(self, q):
        # num, cur: current element with corresponding count
        num = 0
        cur = ''
        ht = defaultdict(int)  # hashtable for the current formula
        ht_inside = None  # hashtable from recursion
        while len(q) > 0:
            c = q.pop(0)
            if c.isdigit():
                num = num*10+int(c)  # multi-digits number
            elif 65 <= ord(c) <= 90:
                # put current element with corresponding count into hashtable
                if len(cur) > 0:
                    ht[cur] += max(num, 1)
                    num = 0
                # put ht_inside to hashtable
                elif ht_inside != None:
                    for key in ht_inside:
                        ht[key] += ht_inside[key] * max(num, 1)
                    ht_inside = None
                    num = 0
                # this char is a big capital letter, start of the cur element
                cur = c
            elif 97 <= ord(c) <= 122:
                cur += c
            elif c == '(':
                # put current element with corresponding count into hashtable
                if len(cur) > 0:
                    ht[cur] += max(num, 1)
                    num = 0
                # put ht_inside to hashtable
                elif ht_inside != None:
                    for key in ht_inside:
                        ht[key] += ht_inside[key] * max(num, 1)
                    ht_inside = None
                    num = 0
                # reset cur element
                cur = ''
                # put to ht_inside
                ht_inside = self.recur(q)
            elif c == ')':
                break

        # put current element with corresponding count into hashtable
        if len(cur) > 0:
            ht[cur] += max(num, 1)
            num = 0
        # put ht_inside to hashtable
        elif ht_inside != None:
            for key in ht_inside:
                ht[key] += ht_inside[key] * max(num, 1)
            ht_inside = None
            num = 0
        return ht


a = 'H2O'
print(Solution().countOfAtoms(a))

a = 'HOH'
print(Solution().countOfAtoms(a))

a = 'HHO'
print(Solution().countOfAtoms(a))

a = 'H1HO'
print(Solution().countOfAtoms(a))

a = 'H2HO'
print(Solution().countOfAtoms(a))

a = 'MgAO2HC3'
print(Solution().countOfAtoms(a))

a = 'Mg(OH)2'
print(Solution().countOfAtoms(a))

a = 'Mg(OH)2A'
print(Solution().countOfAtoms(a))

a = 'Mg(OH)A'
print(Solution().countOfAtoms(a))

a = 'K4(ON(SO3)2)2'
print(Solution().countOfAtoms(a))
