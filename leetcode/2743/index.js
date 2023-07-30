/**
 * @param {string} s
 * @return {number}
 */
var numberOfSpecialSubstrings = function(s) {
    let res = 0
    let j = 0
    const ctr = {}
    for (let i = 0; i < s.length; i++) {
        const c = s[i]
        if (c in ctr === false) {
            ctr[c] = 0
        }
        ctr[c] += 1
        while (ctr[c] > 1) {
            const left = s[j]
            ctr[left] -= 1
            j += 1
        }
        res += i - j + 1
    }
    return res
};