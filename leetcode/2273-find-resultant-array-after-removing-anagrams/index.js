/*
    hashtable

    Time    O(N)
    Space   O(N)
    78 ms, faster than 85.71%
*/
var removeAnagrams = function(words) {
    const res = []
    let prev_sign = null
    for (const w of words) {
        const sign = get_signature(w)
        if (prev_sign != null && sign == prev_sign) {
            continue
        }
        prev_sign = sign
        res.push(w)
    }
    return res
};

const get_signature = w => {
    const chars = Array(26).fill(0)
    for (let c of w) {
        const idx = c.charCodeAt() - 'a'.charCodeAt()
        chars[idx] += 1
    }
    return chars.join(',')
}