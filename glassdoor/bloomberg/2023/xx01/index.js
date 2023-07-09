/*
    There is a string which only contains 0, 1 and '?', where, ? can be 0 or 1

    Given a string s, console.log all the possibilities.

    ref:
    https://leetcode.com/discuss/interview-question/2773700/Bloomberg-London-or-Phone-or-New-Grad

    e.g.
    Input: '??01'
    Output: ['0001', '0101', '1001', '1101']

    Input: '01?0'
    Output: ['0100', '0110']

    Input: '0??0'
    Output: ['0000', '0010', '0100', '0110']
*/
const findAllPermutations = s => {
    const res = []
    const f = (i, sub) => {
        if (i === s.length) {
            return res.push(sub)
        }
        if (s[i] === '?') {
            f(i+1, sub + '0')
            f(i+1, sub + '1')
        } else {
            f(i+1, sub + s[i])
        }
    }
    f(0, '')
    return res
}

console.log(findAllPermutations('??01'))
console.log(findAllPermutations('01?0'))
console.log(findAllPermutations('0??0'))
let t0 = performance.now();
console.log(findAllPermutations('?'.repeat(24)))
let t1 = performance.now();
console.log(`Call to findAllPermutations took ${t1 - t0} milliseconds.`);


console.log("----- another approach -----")

/*
    2nd: DP
    
    However, it is not faster, the reason is we need to print all the possibilities

    e.g.
    - Call to findAllPermutations took 5981.237937927246 milliseconds.
    - Call to findAllPermutations2 took 6665.011711001396 milliseconds.
*/
const findAllPermutations2 = s => {
    const cache = {}
    const f = i => {
        if (i === s.length) {
            return ['']
        }
        if (i in cache) {
            return cache[i]
        }
        const sub_result = []
        if (s[i] === '?') {
            const A = f(i+1)
            for (let sub of A) {
                sub_result.push(sub + '0')
                sub_result.push(sub + '1')
            }
        } else {
            const A = f(i+1)
            for (let sub of A) {
                sub_result.push(sub + s[i])
            }
        }
        cache[i] = sub_result
        return sub_result
    }
    return f(0)
}

console.log(findAllPermutations2('??01'))
console.log(findAllPermutations2('01?0'))
console.log(findAllPermutations2('0??0'))
t0 = performance.now();
console.log(findAllPermutations2('?'.repeat(24)))
t1 = performance.now();
console.log(`Call to findAllPermutations2 took ${t1 - t0} milliseconds.`);