/**
 * @param {any} obj1
 * @param {any} obj2
 * @return {any}
 */
var deepMerge = function(obj1, obj2) {
    if (obj1 !== undefined && obj2 === undefined) {
        return obj1
    }
    if (obj1 === undefined && obj2 !== undefined) {
        return obj2
    }
    if (obj1 === null || obj2 === null) {
        return obj2
    }
    if (Array.isArray(obj1) && Array.isArray(obj2)) {
        const n = Math.max(obj1.length, obj2.length)
        const res = []
        for (let i = 0; i < n; i++) {
            // console.log(obj1[i], obj2[i])
            const node = deepMerge(obj1[i], obj2[i])
            res.push(node)
        }
        return res
    }
    if (typeof obj1 === 'object' && Array.isArray(obj1) === false
        && typeof obj2 === 'object' && Array.isArray(obj2) === false
    ) {
        console.log(obj1, obj2)
        const keys = new Set([...Object.keys(obj1), ...Object.keys(obj2)])
        const res = {}
        for (let key of keys) {
            if (key in obj1 && key in obj2) {
                res[key] = deepMerge(obj1[key], obj2[key])
            } else if (key in obj1 && key in obj2 === false) {
                res[key] = obj1[key]
            } else {
                res[key] = obj2[key]
            }
        }
        return res
    }
    return obj2
};

/**
 * let obj1 = {"a": 1, "c": 3}, obj2 = {"a": 2, "b": 2};
 * deepMerge(obj1, obj2); // {"a": 2, "c": 3, "b": 2}
 */