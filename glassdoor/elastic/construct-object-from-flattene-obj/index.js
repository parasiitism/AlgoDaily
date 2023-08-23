/*
    How to flatten a nested JS object into an object keys in dot notation.

    e.g. input : { 
        'a.b': 1, 
        'a.c.d': 2, 
        'a.c.e.f': 3, 
        'g': 4
    }

    output = {
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
*/
const construct = obj => {
    const root = {}
    for (let key in obj) {
        const path = key.split('.')
        let curNode = root
        for (let i = 0; i < path.length; i++) {
            const x = path[i]
            if (x in curNode === false) {
                if (i+1 == path.length) {
                    curNode[x] = obj[key]
                } else {
                    curNode[x] = {}
                }
            }
            curNode = curNode[x]
        }
    }
    return root
}

input = {
    'a.b': 1,
    'a.c.d': 2,
    'a.c.e.f': 3,
    'g': 4
}
console.log(JSON.stringify(construct(input)))
/*
    output = {
        "a": {
            "b":1,
            "c": {
                "d":2,
                "e":{
                    "f":3
                }
            }
        },
        "g":4
    }
*/