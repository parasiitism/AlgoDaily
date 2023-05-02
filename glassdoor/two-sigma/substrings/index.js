/*
    Given a string of lowercase characters, return 2 substrings which
    - min-length substring that starts with a vowel and end with a consonant
    - max-length substring that starts with a vowel and end with a consonant

    e.g.1
    Input: abc
    Output: [ 'ab', 'abc' ]

    e.g.2
    Input: xyzaabcde
    Output: [ 'ab', 'aabcd' ]
*/
const f = S => {
    const n = S.length
    let vowel_first_idx = -1
    let vowel_last_idx = -1
    let min_length_sub = null
    let max_length_sub = null
    for (let i = 0; i < n; i++) {
        const c = S[i]
        if ('aeiou'.indexOf(c) > -1) {
            if (vowel_first_idx === -1) {
                vowel_first_idx = i
            }
            vowel_last_idx = i
        } else {
            if (vowel_first_idx === -1) {
                continue
            }
            const short_sub = S.slice(vowel_last_idx, i+1)
            if (min_length_sub === null) {
                min_length_sub = short_sub
                max_length_sub = short_sub
            }
            const long_sub = S.slice(vowel_first_idx, i+1)
            if (long_sub.length > max_length_sub.length) {
                max_length_sub = long_sub
            }
        }
    }
    return [min_length_sub, max_length_sub]
}

console.log(f('abc'))   // [ 'ab', 'abc' ]
console.log(f('abcadef')) // [ 'ab', 'abcadef' ]
console.log(f('zabcadef')) // [ 'ab', 'abcadef' ]
console.log(f('xyzaabcde')) // [ 'ab', 'aabcd' ]