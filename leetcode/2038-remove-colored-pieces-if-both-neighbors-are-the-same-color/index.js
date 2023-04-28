/*
    2nd: count AAA and BBB
    - alice wins if an only if AAA >= BBB+1

    Time    O(N)    87ms beats 34.43%
    Space   O(1)
*/

/**
 * @param {string} colors
 * @return {boolean}
 */
var winnerOfGame = function(colors) {
    let alice = 0
    let bob = 0
    for (let i = 1; i < colors.length - 1; i++) {
        if (colors[i-1] === colors[i] && colors[i] === colors[i+1]) {
            if (colors[i] === 'A') {
                alice += 1
            } else {
                bob += 1
            }
        }
    }
    return alice > bob
};