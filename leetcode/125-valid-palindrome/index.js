/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    s = s.toLowerCase()

    let left = 0
    let right = s.length - 1
    while (left < right) {
        const x = isAlphaNumeric(s[left])
        const y = isAlphaNumeric(s[right])
        if (x && y) {
            if (s[left] === s[right]) {
                left += 1
                right -= 1
            } else {
                return false
            }
        } else if (!x) {
            left += 1
        } else if (!y) {
            right -= 1
        }
    }
    return true
};

const isAlphaNumeric = function(c) {
    return c >= 'A' && c <= 'Z' || c >= '0' && c <= '9'
}
