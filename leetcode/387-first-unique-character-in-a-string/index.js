/*
    1st: hashtable

    Time    O(N)
    Space   O(N)
	112 ms, faster than 71.60%
*/
var firstUniqChar = function (s) {
	const ctr = {}
    for (let i = 0; i < s.length; i++) {
        const c = s[i]
        if (c in ctr === false) {
            ctr[c] = 0
        }
        ctr[c] += 1
    }
    for (let i = 0; i < s.length; i++) {
        const c = s[i]
        if (ctr[c] === 1) {
            return i
        }
    }
    return -1
};
