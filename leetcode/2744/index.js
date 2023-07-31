/*
    hashtable

    Time    O(N)
    Space   O(1)
*/
var maximumNumberOfStringPairs = function(words) {
    const seen = new Set()
    let res = 0
    for (let w of words) {
        if (seen.has(w)) {
            res += 1
        }
        const r = reverseStr(w)
        seen.add(r)
    }
    return res
};

const reverseStr = s => {
    let res = ''
    for (let i = s.length-1; i >= 0; i--) {
        res += s[i]
    }
    return res
}