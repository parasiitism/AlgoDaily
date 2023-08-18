/*
    Recursion

    Time    O(N) all nodes
    Space   O(N)
*/
var undefinedToNull = function(obj) {
    if (obj === undefined || obj === null) {
        return null
    }
    if (Array.isArray(obj)) {
        const res = []
        for (let x of obj) {
            const temp = undefinedToNull(x)
            res.push(temp)
        }
        return res
    }
    if (typeof obj === 'object') {
        const res = {}
        const keys = Object.keys(obj)
        for (let k of keys) {
            res[k] = undefinedToNull(obj[k])
        }
        return res
    }
    return obj
};