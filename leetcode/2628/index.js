/**
 * @param {any} o1
 * @param {any} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
    if (o1 === o2) {
        return true;
    }
    // Array is also a type of "object"
    if (typeof o1 !== 'object' || o1 === null || typeof o2 !== 'object' || o2 === null) {
        return false;
    }
    if (Array.isArray(o1) !== Array.isArray(o2)) {
        return false;
    }
    // We can use Object.keys to get the keys of an object OR the arrayitems
    const keys1 = Object.keys(o1)
    const keys2 = Object.keys(o2)
    if (keys1.length !== keys2.length) {
        return false
    }
    for (let k in o1) {
        if (k in o2 === false) {
            return false
        }
    }
    // recursively check the children
    for (let key in o1) {
        const val1 = o1[key]
        const val2 = o2[key]
        const b = areDeeplyEqual(val1, val2)
        if (b === false) {
            return false
        }
    }
    return true
};