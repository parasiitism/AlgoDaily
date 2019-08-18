/**
 * @param {string} A
 * @param {string} B
 * @return {boolean}
 * 
    2nd approach:
    - 2A must contain a rotated string

    Time    O(n)
    Space   O(1)
 60 ms, faster than 37.45%
 */
var rotateString = function (A, B) {
    const C = A + A
    return A.length == B.length && C.includes(B)
};

/**
 * @param {string} A
 * @param {string} B
 * @return {boolean}
 * 
 * 1st approach:
    - rotate A to see if B appears

    Time    O(n)
    Space   O(1)
    56 ms, faster than 56.09%
 */
var rotateString = function (A, B) {
    if (A.length != B.length) {
        return false
    }
    if (A.length == B.length && A.length == 0) {
        return true
    }
    let i = 0
    while (i < A.length) {
        A = A.slice(1) + A[0]
        if (A == B) {
            return true
        }
        i += 1
    }
    return false
};