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
    1st: DFS with space
    - extra param for the path 

    Time    O(N * H) H: height
    Space   O(H + N * H)
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
    1st: DFS with space
    - extra param for the path 

    Time    O(N * H + W) H: height
    Space   O(N)
*/
const flatten2 = object => {
    const res = {}
    const parents = {} // child: parent
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
                // O(H)
                const path = []
                let cur = k
                while (cur != null) {
                    path.push(cur)
                    cur = parents[cur]
                }
                path.reverse()
                res[path.join('.')] = v
            }
        }
    }
    dfs(object, null)
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