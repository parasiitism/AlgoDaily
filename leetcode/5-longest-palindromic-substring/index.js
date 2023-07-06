/*
    1st approach
    - for each charactor, expand its left and right if palindrome

    Time    O(n^2)
    Space   O(1)
    100 ms, faster than 78.74%
*/
var longestPalindrome = function(s) {
    const n = s.length
    let res = ''
    for (let i = 0; i < n; i++) {
        const [L1, R1] = expand(s, i, i)
        const [L2, R2] = expand(s, i, i+1)
        if (R1 - L1 + 1 > res.length) {
            res = s.slice(L1, R1+1)
        }
        if (R2 - L2 + 1 > res.length) {
            res = s.slice(L2, R2+1)
        }
    }
    return res
};

const expand = (s, L, R) => {
    if (s[L] !== s[R]) {
        return [L, L]
    }
    let i = L
    let j = R
    while (i-1 >= 0 && j+1 < s.length && s[i-1] === s[j+1]) {
        i -= 1
        j += 1
    }
    return [i, j]
}
