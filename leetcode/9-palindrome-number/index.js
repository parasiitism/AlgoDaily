/**
 * @param {number} x
 * @return {boolean}
 *  
 *  2 pointers

    Time    O(n) n: number of digits of x
    Space   O(n)
    200 ms, faster than 54.62%
 */
var isPalindrome = function (x) {
    const s = x.toString()
    let i = 0
    let j = s.length - 1
    while (i < j) {
        if (s[i] != s[j]) {
            return false
        }
        i++
        j--
    }
    return true
};