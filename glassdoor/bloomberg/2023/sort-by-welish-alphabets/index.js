/*
    Given a welsh dictionary, sorted in welsh alphabetical order, 
    and a list of words written in the welsh language, sort the list of words in welsh alphabetical 
    
    e.g. 
    Input:
    welshDict = ["a","b","c","ch","d","dd","e", "f", "ff", "g", "ng", "h", "i", "j", "l", "ll", "m", "n", "o", "p", "ph", "r", "rh", "s", "t", "th", "u", "w", "y"]
    words = ["ddr", "nah", "dea", "dd", "ngah"]

    Output: ["dea", "dd", "ddr", "ngah", "nah"]
    

    ref: https://leetcode.com/discuss/interview-question/682583/bloomberg-phone-order-list-in-welsh-alphabetical-order
*/
const f = (welshDict, words) => {
    const dict = {}
    for (let i = 0; i < welshDict.length; i++) {
        const w = welshDict[i]
        dict[w] = i
    }

    const process = w => {
        const vals = []
        let i = 0
        while (i < w.length) {
            if (i+1 < w.length && w[i]+w[i+1] in dict) {
                const order = dict[w[i]+w[i+1]]
                vals.push(order)
                i += 1
            } else if (w[i] in dict) {
                const order = dict[w[i]]
                vals.push(order)
            }
            i += 1
        }
        return vals
    }

    words.sort((a, b) => {
        const valuesA = process(a)
        const valuesB = process(b)

        const minLength = Math.min(valuesA.length, valuesB.length)
        for (let i = 0; i < minLength; i++) {
            if (valuesA[i] != valuesB[i]) {
                return valuesA[i] - valuesB[i]
            }
        }
        return valuesA.length - valuesB.length
    })

    return words
}

let a = ["a","b","c","ch","d","dd","e", "f", "ff", "g", "ng", "h", "i", "j", "l", "ll", "m", "n", "o", "p", "ph", "r", "rh", "s", "t", "th", "u", "w", "y"]
let b = ["ddr", "nah", "dea", "dd", "ngah"]
console.log(f(a, b))  // ["dea", "dd", "ddr", "ngah", "nah"]
/*
dea: [4, 6, 0]
dd: [5]
ddr: [5, 21]
ngah: [10, 0, 11]
nah: [17,0,11]
*/