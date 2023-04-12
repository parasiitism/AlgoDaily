/*
    1st: bit op + sort
    1. count the number of bits for each number from input
    2. sort the input

    Time    O(NlogN * logX)
    Space   O(1)
    424 ms, faster than 5.26%
*/
var sortByBits = function(arr) {
    return arr.sort((a, b) => {
        const x = count_ones(a)
        const y = count_ones(b)
        if (x != y) {
            return x - y
        }
        return a - b
    })
};

const count_ones = n => {
    let ones = 0
    while (n > 0) {
        if (n % 2 == 1) {
            ones += 1
        }
        n = Math.floor(n/2)
    }
    return ones
}