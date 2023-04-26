/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
    const counter = {}
    let j = 0
    let res = 0
    for (let i = 0; i < s.length; i++) {
        const c = s[i]
        if (c in counter === false) {
            counter[c] = 0
        }
        counter[c] += 1
        while (counter[c] > 1) {
            const left = s[j]
            j += 1
            counter[left] -= 1
            if (counter[left] === 0) {
                delete counter[left]
            }
        }
        res = Math.max(res, i - j + 1)
    }
    return res
};


/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const n = s.length
    const ctr = Array(128).fill(0)
    let j = 0
    let res = 0
    for (let i=0; i < n; i ++) {
        const c = s[i]
        const idx = c.charCodeAt()
        ctr[idx] += 1
        while (ctr[idx] > 1) {
            const left = s[j]
            const left_idx = left.charCodeAt()
            ctr[left_idx] -= 1
            j += 1
        }
        res = Math.max(res, i - j + 1)
    }
    return res
};