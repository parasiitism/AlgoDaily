/*
    sort

    Time    O(N + VlogV)
    Space   O(V)
*/
var sortVowels = function(s) {
    const vowels = []
    for (let c of s) {
        if ('aeiouAEIOU'.indexOf(c) > -1) {
            vowels.push(c)
        }
    }
    vowels.sort((a, b) => a.charCodeAt() - b.charCodeAt())
    let res = ''
    for (let c of s) {
        if ('aeiouAEIOU'.indexOf(c) > -1) {
            res += vowels.shift()
        } else {
            res += c
        }
    }
    return res
};