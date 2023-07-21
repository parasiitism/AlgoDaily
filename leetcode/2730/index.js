/**
 * @param {string} s
 * @return {number}
 */
var longestSemiRepetitiveSubstring = function(s) {
    const n = s.length
    let j = 0
    let sameCnt = 0
    let res = 1
    for (let i = 1; i < n; i++) {
        if (s[i-1] == s[i]) {
            sameCnt += 1
        }
        while (sameCnt > 1) {
            const left = s[j]
            j += 1
            if (left === s[j]) {
                sameCnt -= 1
            }
        }
        res = Math.max(res, i - j + 1)
    }
    return res
};