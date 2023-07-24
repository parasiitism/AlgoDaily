/*
    2nd approach: sliding window
    - similar to lc438, 567
    - check if each substring is an anagram but dont use slice in every iteration

    Time    O(n*m)
    Space   O(m)
    208 ms, faster than 37.02% 
*/
/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    const n = s.length
    const k = p.length
    
    const targetCtr = Array(26).fill(0)
    for (let c of p) {
        const idx = c.charCodeAt() - 'a'.charCodeAt()
        targetCtr[idx] += 1
    }

    const curCtr = Array(26).fill(0)

    const res = []
    let j = 0
    for (let i = 0; i < n; i++) {
        const idx = s[i].charCodeAt() - 'a'.charCodeAt()
        curCtr[idx] += 1
        if (i - k >= 0) {
            const idx2 = s[i-k].charCodeAt() - 'a'.charCodeAt()
            curCtr[idx2] -= 1
        }
        if (ifAreAnagram(targetCtr, curCtr)) {
            res.push(i-k+1)
        }
    }
    return res
};

const ifAreAnagram = (A, B) => {
    for (let i = 0; i < 26; i++) {
        if (A[i] !== B[i]) {
            return false
        }
    }
    return true
}