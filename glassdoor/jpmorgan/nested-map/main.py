"""
    there are diff versions of removing things from a nested hashmap
    
    version1: remove int

    takeaway:
    1. isinstance() vs type():
        - use isinstance() instead of type() because type() cannot identify parent class(lack of support for inheritance)
        - https://www.geeksforgeeks.org/type-isinstance-python/
    2. boolean is regarded as int out of historic reason
        - need special handling for bool
        - https://stackoverflow.com/questions/37888620/comparing-boolean-and-int-using-isinstance
"""


def removeInt(node):
    m = {}
    for key in node:
        if isinstance(node[key], int) == False or isinstance(node[key], bool) == True:
            if isinstance(node[key], dict) == True:
                temp = removeInt(node[key])
                m[key] = temp
            else:
                m[key] = node[key]
    return m


a = {
    'a': 1,
    'b': {
        'c': 2,
        'd': 'hi',
        'f': {
            'g': 'hello',
            'h': 'word',
        },
        'i': '!!',
    },
    'k': True
}

"""
result
{
    'b': {
    'i': '!!',
    'd': 'hi',
    'f': {
         'h': 'word',
         'g': 'hello'
        }
    }
}
"""

print(removeInt(a))

print("-----")

"""
    version2: print
"""


def printMap(node, path):
    for key in node:
        curPath = path + ',' + key
        if isinstance(node[key], dict) == True:
            printMap(node[key], curPath)
        else:
            print(curPath, '=>', node[key])


a = {
    'a': 1,
    'b': {
        'c': 2,
        'd': 'hi',
        'f': {
            'g': 'hello',
            'h': 'word',
        },
        'i': '!!',
    },
    'k': True
}

print(printMap(a, ''))

print("-----")

"""
    version3: nested list
"""


def dfs(arr):
    for x in arr:
        if isinstance(x, list):
            dfs(x)
        else:
            print(x)


a = [
    [1, 2],
    3,
    [4, [5, 6]],
]
dfs(a)

print("------")

"""
    version4: nested list iterater

    approach:
    
    e.g. a = [[[1,2],3],4,[5,6]]

    in the beginning
    stack = [a]

    when we do hasnext(), we unfold the top item until we get to an integer
    stack = [
        [[1,2],3],          <- top
        4,
        [5,6]
    ]

    stack = [
        [1,2],              <- top
        3,
        4,
        [5,6]
    ]

    stack = [
        1,                  <- top, done unfolding
        2,
        3,
        4,
        [5,6],
    ]
"""


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        for i in range(len(nestedList)-1, -1, -1):
            item = nestedList[i]
            self.stack.append(item)

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        while len(self.stack) > 0:
            top = self.stack[-1]
            if isinstance(top, int):
                return True
            else:
                pop = self.stack.pop()
                for i in range(len(pop)-1, -1, -1):
                    item = pop[i]
                    self.stack.append(item)
        return False


a = [
    [1, 2],
    3,
    [4, [5, 6]],
]
s = NestedIterator(a)

while s.hasNext():
    print(s.next())
