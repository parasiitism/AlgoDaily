/*
    2nd: prefix sum + mod

    Time    O(NlogM)
    Space   O(N)
*/
var divisibilityArray = function(word, m) {
    const n = word.length
    const res = []
    let pfs = 0
    for (let i = 0; i < n; i++) {
        pfs = pfs * 10 + parseInt(word[i])
        pfs = pfs % m
        if (pfs == 0) {
            res.push(1)
        } else {
            res.push(0)
        }
    }
    return res
};