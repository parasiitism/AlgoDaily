/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
    const m = {}
    return f(n, m)
};

var f = function (n, m) {
    if (n == 0) {
        return 1
    } else if (n < 0) {
        return 0
    }
    if (m[n]) {
        return m[n]
    }
    total = f(n - 1, m) + f(n - 2, m)
    m[n] = total
    return total
}