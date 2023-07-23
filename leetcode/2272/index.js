/*
    1st: brute-force with a hashtable

    Time    O(26 * N^2)
    Space   O(N)
    TLE 122 / 138 testcases passed
*/
var largestVariance = function(s) {
    const n = s.length
    let res = 0
    for (let i = 0; i < n; i++) {
        const ctr = Array(26).fill(0)
        for (let j = i; j < n; j++) {
            const c = s[j]
            const idx = c.charCodeAt() - 'a'.charCodeAt()
            ctr[idx] += 1
            const freqs = ctr.filter(x => x > 0)
            const low = Math.min(...freqs)
            const high = Math.max(...freqs)
            res = Math.max(res, high - low)
        }
    }
    return res
};