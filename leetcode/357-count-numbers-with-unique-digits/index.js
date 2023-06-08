/*
    1st approach: math
*/
var countNumbersWithUniqueDigits = function(n) {
    if (n === 0) {
        return 1
    }
    let res = 10
    let start = 9
    for (let i = 1; i < n; i++) {
        start = start * (10 - i)
        res += start
    }
    return res
};