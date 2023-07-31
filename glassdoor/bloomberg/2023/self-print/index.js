/*
    The Input is given as a 2D matrix with True and False values, 
    a interger variable n representing the number of iteration.

    The output should print the pattern in n-th iteration. 
    The iteration follow the following rules:

    Each X representing a True Value and a Blank represents False. 
    In n-th each iteration, the true value of (n-1)-th iteration will be replaced by a copy of entire n-1 iteration itself.

                XXX XXX XXX
                X X X X X X
                XXX XXX XXX
    XXX         XXX     XXX
    X X    ->   X X     X X     ->  ...
    XXX         XXX     XXX
                XXX XXX XXX
                X X X X X X
                XXX XXX XXX
    
    ref:
    - https://leetcode.com/discuss/interview-question/3102633/Bloomberg-or-SDE-Onsite-or-Self-Print
*/
const selfPrint = (pattern, n) => {
    const L = pattern.length
    for (let _ = 0; _ < n-1; _++) {
        const pattern2 = []
        const L2 = pattern.length * L
        for (let _ = 0; _ < L2; _++) {
            pattern2.push(Array(L2).fill(false))
        }
        for (let i = 0; i < pattern.length; i++) {
            for (let j = 0; j < pattern[0].length; j++) {
                if (pattern[i][j] === false) {
                    continue
                }
                for (let i2 = 0; i2 < L; i2++) {
                    for (let j2 = 0; j2 < L; j2++) {
                        pattern2[i*L+i2][j*L+j2] = pattern[i2][j2] // the crux
                    }
                }
            }
        }
        pattern = pattern2
    }
    pattern.forEach(row => {
        let s = ''
        for (let c of row) {
            s += c ? 'X' : ' '
        }
        console.log(s)
    });
}

let a = [[true, true, true], [true, false, true], [true, true, true]]
let b = 1
console.log(selfPrint(a, b))

a = [[true, true, true], [true, false, true], [true, true, true]]
b = 2
console.log(selfPrint(a, b))

a = [[true, true, true], [true, false, true], [true, true, true]]
b = 3
console.log(selfPrint(a, b))

console.log('-----')

a = [[true, true], [true, false]]
b = 1
console.log(selfPrint(a, b))

a = [[true, true], [true, false]]
b = 2
console.log(selfPrint(a, b))

a = [[true, true], [true, false]]
b = 3
console.log(selfPrint(a, b))

a = [[true, true], [true, false]]
b = 4
console.log(selfPrint(a, b))