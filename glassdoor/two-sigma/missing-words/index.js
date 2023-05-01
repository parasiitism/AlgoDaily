/*
    Given 2 sentenses, T is a subsequence of S, remove every word which 1st-appreared from T in S

    e.g.1
    Input:
    S = I like eating cheese do you like cheese
    T = like cheese

    Output:
    i eating do you like cheesese

    e.g.2
    Input:
    S = I like soft cheese and hard cheese yum
    T = like cheese yum

    Output:
    i eating do you like cheesese
*/
const f = (S, T) => {
    const A = S.split(' ')
    const B = T.split(' ')
    let i = 0
    let j = 0
    const res = []
    while (i < A.length) {
        if (A[i] === B[j]) {
            j += 1
        } else {
            res.push(A[i])
        }
        i += 1
    }
    return res.join(' ')
}

console.log(f('i like eating cheese do you like cheese', 'like cheese'))
console.log(f('I like soft cheese and hard cheese yum', 'like cheese yum'))
