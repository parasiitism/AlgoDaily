/*
    Reverse a string, double every second digit, sum all of them

    e.g.
    4567 -> 7654 -> 7 + 6*2 + 5 + 4*2 = 7 + (1+2) + 5 + 8 = 23
*/
const f = S => {
    const n = S.length
    let res = 0
    for (let i = n-1; i >= 0; i--) {
        let d = parseInt(S[i])
        const j = n-1-i
        if (j % 2 == 0) {
            res += d
        } else {
            d *= 2
            const tenth = Math.floor(d / 10)
            const digit = d % 10
            res += tenth + digit
        }
    }
    return res
}
console.log(f("4567"))