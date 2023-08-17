/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const n = s.length
    const ctr = {}
    let j = 0
    let res = 0
    for (let i = 0; i < n; i++) {
        const c = s[i]
        ctr[c] = ctr[c] ? ctr[c]+1 : 1
        while (ctr[c] > 1) {
            const left = s[j]
            ctr[left] -= 1
            j += 1 
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