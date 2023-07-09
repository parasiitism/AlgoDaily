/*
    Given a welsh dictionary, sorted in welsh alphabetical order, 
    and a list of words written in the welsh language, sort the list of words in welsh alphabetical order

    ref: https://leetcode.com/discuss/interview-question/682583/bloomberg-phone-order-list-in-welsh-alphabetical-order
*/
const sortByWelish = input => {
    const welsh = ["a","b","c","ch","d","dd","e", "f", "ff", "g", "ng", "h", "i", "j", "l", "ll", "m", "n", "o", "p", "ph", "r", "rh", "s", "t", "th", "u", "w", "y"]

    const dict = {}
    for (let i = 0 ; i < welsh.length; i++) {
        dict[welsh[i]] = i
    }

    const process = word => {
        const vals = []
        let i = 0
        while (i < word.length) {
            if (i+1 < word.length && word[i]+word[i+1] in dict) {
                vals.push(dict[word[i] + word[i+1]])
                i += 2
            } else if (word[i] in dict) {
                vals.push(dict[word[i]])
                i += 1
            }
        }
        return vals
    }

    input.sort((a, b) => {
        const A = process(a)
        const B = process(b)
        
        const minLength = Math.min(A.length, B.length)
        for (let i = 0; i < minLength; i++) {
            if (A[i] !== B[i]) {
                return A[i] - B[i]
            }
        }
        return A.length - B.length
    })

    return input
}

console.log(sortByWelish(["ddr", "nah", "dea", "dd", "ngah"]))  // ["dea", "dd", "ddr", "ngah", "nah"]
/*
dea: [4, 6, 0]
dd: [5]
ddr: [5, 21]
ngah: [10, 0, 11]
nah: [17,0,11]
*/