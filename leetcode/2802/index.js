/*
    binary reduction
    - e.g. the way to create priority queue

    Time    O(logN)
    Space   O(logN)
*/
var kthLuckyNumber = function(k) {
    const res = []
    while (k > 0) {
        const d = k % 2
        k = Math.floor((k-1)/2)
        if (d == 0) {
            res.push('7')
        } else {
            res.push('4')
        }
    }
    return res.reverse().join('')
};
