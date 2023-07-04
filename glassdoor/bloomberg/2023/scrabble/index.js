/*
    Given a dictionary, find longest matching word from dictionary for given set of chars.
    e.g.
    dict={when, what, whatthen, whatnow}, input="whatno", expected output= "what"
    dict={when, what, whatthen, whatnow}, input="whatnwo", expected output= "whatnow"
    dict={when, what, whatthen, whatnow}, input="wonthaw", expected output= "whatnow"

    ref:
    - https://leetcode.com/discuss/interview-question/3099518/Bloomberg-or-Phone-1st-round-Hackerrank-or-Scrabble

-------- questions to ask --------

    1. a word might appear more than once in dict? 
    2. lowercase / upper case?
*/
const scrabble = (dict, input) => {
    let res = ''
    const ctr_input = countChars(input)
    dict.forEach((w) => {
        const ctr = countChars(w)
        if (ifAHasB(ctr_input, ctr)) {
            if (w.length > res.length) {
                res = w
            }
        }
    })
    return res
}

const countChars = word => {
    const ctr = Array(26).fill(0)
    for (let c of word) {
        const i = c.charCodeAt() - 'a'.charCodeAt()
        ctr[i] += 1
    }
    return ctr
}

const ifAHasB = (A, B) => {
    for (let i = 0; i < 26; i++) {
        if (A[i] < B[i]) {
            return false
        }
    }
    return true
}

let a = new Set(['when', 'what', 'whatthen', 'whatnow'])
let b = 'whatno'
console.log(scrabble(a, b))

b = 'whatnwo'
console.log(scrabble(a, b))

b = 'wonthaw'
console.log(scrabble(a, b))
