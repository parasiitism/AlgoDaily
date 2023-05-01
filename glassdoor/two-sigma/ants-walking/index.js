/*
    Given a string, there are some ants on each end and they walk toward another side of the string every second
    Print the snapshot of string at every second
    
    < or >  means an ant
    +       means ants overlap
    .       means string unit 

    Step 1: ">>.....<<"
    Step 2: ".>>...<<."
    Step 3: "..>>.<<.."
    Step 4: "...>+<..."
    Step 5: "...<+>..."
    Step 6: "..<<.>>.."
*/
const f = S => {
    const n = S.length
    const res = [S]
    let left_ants = []
    let right_ants = []
    for (let i=0; i < n; i++) {
        if (S[i] === '>') {
            left_ants.push(i)
        } else if (S[i] === '<') {
            right_ants.push(i)
        }
    }
    for (let i = 1; i < n; i++) {
        left_ants = left_ants.map(x => x+1)
        right_ants = right_ants.map(x => x-1)
        const counter = {}
        count_ants_on_string(counter, left_ants, '>')
        count_ants_on_string(counter, right_ants, '<')

        let snapshot = ''
        for (let j = 0; j < n; j++) {
            if (j in counter) {
                if (counter[j].length > 1) {
                    snapshot += '+'
                } else {
                    const ant = counter[j][0]
                    snapshot += ant
                }
            } else {
                snapshot += '.'
            }
            // IF NEEDED: count the ants, break here if fewer
        }
        res.push(snapshot)
    }
    return res
}

const count_ants_on_string = (counter, arr, ant) => {
    for (let x of arr) {
        if (x in counter === false) {
            counter[x] = []
        }
        counter[x].push(ant)
    }
}

console.log(f('>>.....<<'))
console.log(f('>>......<<'))
console.log(f('>..>...<'))