/*
    1st: hashtable
    - count the number fo each character
    - subtract the source from target, to get the diff

    Time    O(S+T)
    Space   O(S+T)
    104 ms, faster than 84.16%
*/
var minSteps = function(s, t) {
    const A = countChars(s)
    const B = countChars(t)
    let diffs = 0
    for (let i=0; i < 26; i++) {
        diffs += Math.abs(A[i] - B[i])
    }
    return diffs / 2
};
const countChars = s => {
    const ctr = Array(26).fill(0)
    for (let c of s) {
        const i = c.charCodeAt() - 'a'.charCodeAt()
        ctr[i] += 1
    }
    return ctr
}