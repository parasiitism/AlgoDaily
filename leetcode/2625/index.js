/*
    1st: recursion
*/
var flat = function(arr, n) {
    const res = [];
    for (let x of arr) {
        if (Array.isArray(x) && n > 0) {
            res.push(...flat(x, n - 1))
        } else {
            res.push(x)
        }
    }
    return res
};