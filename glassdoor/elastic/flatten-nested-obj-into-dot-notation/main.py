"""
    How to flatten a nested JS object into an object keys in dot notation.

    e.g. input = {
        a: {
            b: 1,
            c: {
                d: 2,
                e: {
                    f: 3
                }
            }
        },
        g: 4
    }

    output: {
        'a.b': 1,
        'a.b.c.d': 2,
        'a.b.c.e.f': 3,
        'g': 4
    }

    questions to ask:
    - will there be other types: array, undefined, null...etc
"""

"""
    0th: recursion

    Time    O(N * H)
    Space   O(H * K^2)
"""


def flatten0(obj):
    res = {}

    def dfs(node, path):
        for key in node:
            val = node[key]
            new_path = path + '.' + key if len(path) > 0 else key
            if isinstance(val, dict):
                dfs(val, new_path)
            else:
                res[new_path] = val
    dfs(obj, '')

    return res


input0 = {
    'a': {
        'b': 1,
        'c': {
            'd': 2,
            'e': {
                'f': 3
            }
        }
    },
    'g': 4
}
print(flatten0(input0))

print('---')

"""
    0th: recursion

    Time    O(N * H)
    Space   O(H * K^2)
"""


def flatten1(obj):

    parents = {}  # { child: parent } e.g. b:a
    leaves = []

    def dfs(node, parent):
        for key in node:
            val = node[key]
            parents[key] = parent
            if isinstance(val, dict):
                dfs(val, key)
            else:
                leaves.append((val, key))
    dfs(obj, None)

    res = {}
    for leave in leaves:
        val, node = leave
        cur = node
        path = []
        while cur != None:
            path.append(cur)
            cur = parents[cur]
        path.reverse()
        key = '.'.join(path)
        res[key] = val
    return res


input0 = {
    'a': {
        'b': 1,
        'c': {
            'd': 2,
            'e': {
                'f': 3
            }
        }
    },
    'g': 4
}
print(flatten1(input0))
