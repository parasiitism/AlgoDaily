/*
    naive approach

    Time    O(n!)
    Space   O(n)
    76 ms, faster than 48.45%
*/
var generate = function(numRows) {
    const res = []
    for (let i = 1; i <= numRows; i++) {
        const row = Array(i).fill(1)
        const above = res.length > 0 ? res[res.length-1]: []
        for (let j = 1; j < i-1; j++) {
            row[j] = above[j-1] + above[j]
        }
        res.push(row)
    }
    return res
};
