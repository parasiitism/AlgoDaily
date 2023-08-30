/*
    string

    Time    O(N)
    Space   O(N) the result
*/
var splitWordsBySeparator = function(words, separator) {
    const res = []
    for (let s of words) {
        const words = s.split(separator)
        for (let w of words) {
            if (w.length > 0) {
                res.push(w)
            }
        }
    }
    return res
};