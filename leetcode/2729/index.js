/**
 * @param {number} n
 * @return {boolean}
 */
var isFascinating = function(n) {
    const a = n * 2
    const b = n * 3
    const digits = Array(10).fill(0)
    const arr = [n, a, b]
    for (let x of arr) {
        while (x > 0) {
            const d = x % 10
            digits[d] += 1
            x = Math.floor(x / 10)
        }
    }
    for (let i = 1; i <= 9; i++) {
        if (digits[i] !== 1) {
            return false
        }
    }
    return true
};