/**
 * @param {number} N
 * @return {number}
 */
var binaryGap = function (N) {
    let lastOne = -1
    let count = 0
    let i = 0
    while (N > 0) {
        if (N & 1 == 1) {
            if (lastOne != -1) {
                let temp = i - lastOne
                if (temp > count) {
                    count = temp
                }
            }
            lastOne = i
        }
        N = N >> 1
        i++
    }
    return count
};