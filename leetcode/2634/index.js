/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const res = []
    for (let i = 0; i < arr.length; i++) {
        const x = arr[i]
        const b = fn(x, i)
        if (b) {
            res.push(x)
        }
    }
    return res
};