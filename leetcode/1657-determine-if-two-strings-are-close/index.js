/*
    1st: hashtable

    approach for operation 1:
    - as long as they are anagram, we can swap any number of times to make them equal
   
    approach for operation 2:
    - as long as the chars-frequency of S and T are the same, we can swap the frequencies any number of times to make them equal

    Time     O(SlogS + TlogT)
    Space    O(S+T)
    560 ms, faster than 34.78% 
*/
var closeStrings = function(word1, word2) {
    if (word1.length !== word2.length) {
        return false
    }
    const n = word1.length
    const ht1 = {}
    const ht2 = {}
    for (let i = 0; i < n; i++) {
        const a = word1[i]
        const b = word2[i]
        if (a in ht1 === false) {
            ht1[a] = 0
        }
        if (b in ht2 === false) {
            ht2[b] = 0
        }
        ht1[a] += 1
        ht2[b] += 1
    }
    // operation 1
    for (let key in ht1) {
        if (key in ht2 === false) { return false}
    }
    for (let key in ht2) {
        if (key in ht1 === false) { return false}
    }
    // operation 2
    const A = Object.values(ht1)
    const B = Object.values(ht2)
    A.sort((a, b) => a - b)
    B.sort((a, b) => a - b)

    return A.join(",") === B.join(",")
};