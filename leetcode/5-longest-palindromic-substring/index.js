/*
    1st approach
    - for each charactor, expand its left and right if palindrome

    Time    O(n^2)
    Space   O(1)
    100 ms, faster than 78.74%
*/
var longestPalindrome = function(s) {
    let resL = 0
    let resR = 0
    for (let i = 0; i < s.length ; i++) {
        const [L1, R1] = expand(s, i, i)
        const [L2, R2] = expand(s, i, i+1)
        if (R1 - L1 > resR - resL) {
            resR = R1
            resL = L1
        }
        if (R2 - L2 > resR - resL) {
            resR = R2
            resL = L2
        }
    }
    return s.slice(resL, resR+1)
};

const expand = (s, L, R) => {
    if (R == n || s[L] != s[R]) {
        return [L, L]
    }
    while (L-1 >= 0 && R+1 < s.length && s[L-1] == s[R+1]) {
        L -= 1
        R += 1
    }
    return [L, R]
}
