/*
    1st: hashtable

    Time    O(N)
    Space   O(N)
*/
var checkAlmostEquivalent = function(word1, word2) {
    const A = get_signature(word1)
    const B = get_signature(word2)
    for (let i=0; i < 26; i++) {
        if (Math.abs(A[i] - B[i]) > 3) {
            return false
        }
    }
    return true
};

const get_signature = w => {
    const chars = Array(26).fill(0)
    for (let c of w) {
        const idx = c.charCodeAt() - 'a'.charCodeAt()
        chars[idx] += 1
    }
    return chars
}