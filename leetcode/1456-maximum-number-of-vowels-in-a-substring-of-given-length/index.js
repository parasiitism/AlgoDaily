/*
    1st: sliding window

    Time    O(N)
    Space   O(1)
    468 ms, faster than 100.00%
*/
var maxVowels = function(s, k) {
    let cur = 0
    let res = 0
    for (let i = 0 ; i < s.length; i++) {
        const right = s[i]
        if ("aeiou".indexOf(right) > -1) {
            cur += 1
        }
        if (i - k >= 0) {
            const left = s[i-k]
            if ("aeiou".indexOf(left) > -1) {
                cur -= 1
            }
        }
        if (i >= k - 1) {
            res = Math.max(res, cur)
        }
    }
    return res
};