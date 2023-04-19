/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    s = s.toUpperCase()
    let i = 0
    let j = s.length - 1
    while (i <= j) {
        if (!isAlphaNumeric(s[i])) {
            i += 1
        } else if (!isAlphaNumeric(s[j])) {
            j -= 1
        } else {
            if (s[i] !== s[j]) {
                return false
            } else {
                i += 1
                j -= 1
            }
        }
    }
    return true
};

const isAlphaNumeric = function(c) {
    return c >= 'A' && c <= 'Z' || c >= '0' && c <= '9'
}
