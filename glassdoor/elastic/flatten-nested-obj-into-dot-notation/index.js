/*
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
*/

/*
    0th: DFS with space
    - extra param for the path 

    []

    Time    O(N * H) -> O(N^2) H: height
    Space   O(H + N * H^2)
*/
const flatten0 = object => {
    const res = {}
    const dfs = (node, path) => {
        if (!node) {
            return
        }
        const keys = Object.keys(node) // O(W)
        for (let k of keys) {
            const v = node[k]
            const _path = path.length > 0 ? `${path}.${k}` : k // O(N)
            if (typeof v === 'object' && !Array.isArray(v)) {
                dfs(v, _path)
            } else {
                res[_path] = v // O(N)
            }
        }
    }
    dfs(object, '')
    return res
}

input = {
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
console.log(flatten0(input))

console.log('-----')

/*
    1st: DFS with space
    - extra param for the path 

    []

    Time    O(N * H) H: height
    Space   O(H + N * H^2)
*/
const flatten1 = object => {
    const res = {}
    const dfs = (node, path) => {
        if (!node) {
            return
        }
        const keys = Object.keys(node) // O(W)
        for (let k of keys) {
            const v = node[k]
            const _path = [...path, k] // O(N)
            if (typeof v === 'object' && !Array.isArray(v)) {
                dfs(v, _path)
            } else {
                res[_path.join('.')] = v // O(N)
            }
        }
    }
    dfs(object, [])
    return res
}

input = {
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
console.log(flatten1(input))

console.log('-----')

/*
    2nd: DFS + space optimization
    - extra param for the path 

    Time    O(N + WH) W: leaves, H: height; W*H = N actually
    Space   O(N)
*/
const flatten2 = object => {
    const res = {}
    const parents = {} // child: parent
    const leaves = []
    const dfs = (node, p) => {
        if (!node) {
            return
        }
        const keys = Object.keys(node)
        for (let k of keys) {
            const v = node[k]
            parents[k] = p
            if (typeof v === 'object' && !Array.isArray(v)) {
                dfs(v, k)
            } else {
                leaves.push([k, v])
            }
        }
    }
    dfs(object, null)
    for (let [k, v] of leaves) {
        const path = []
        let cur = k
        while (cur != null) {
            path.push(cur)
            cur = parents[cur]
        }
        path.reverse()
        res[path.join('.')] = v
    }
    return res
}

input = {
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
console.log(flatten2(input))

console.log("-----")

const flatten3 = object => {
    const res = {}
    const parents = {} // child: parent
    const leaves = []

    const stack = [[object, null]]
    while (stack.length > 0) {
        const [node, p] = stack.pop()
        const keys = Object.keys(node)
        for (let k of keys) {
            const v = node[k]
            parents[k] = p
            if (typeof v === 'object' && !Array.isArray(v)) {
                stack.push([v, k])
            } else {
                leaves.push([k, v])
            }
        }
    }

    for (let [k, v] of leaves) {
        const path = []
        let cur = k
        while (cur != null) {
            path.push(cur)
            cur = parents[cur]
        }
        path.reverse()
        res[path.join('.')] = v
    }
    return res
}

input = {
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
console.log(flatten3(input))