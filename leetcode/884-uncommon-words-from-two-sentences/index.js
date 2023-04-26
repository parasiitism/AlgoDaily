/**
 * @param {string} s1
 * @param {string} s2
 * @return {string[]}
 */
var uncommonFromSentences = function(s1, s2) {
    const ctr = {}
    for (let c of s1.trim().split(" ")) {
        if (c in ctr === false) {
            ctr[c] = 0
        }
        ctr[c] += 1
    }
    for (let c of s2.trim().split(" ")) {
        if (c in ctr === false) {
            ctr[c] = 0
        }
        ctr[c] += 1
    }
    const res = []
    for (let key in ctr) {
        if (ctr[key] === 1) {
            res.push(key)
        }
    }
    return res
};