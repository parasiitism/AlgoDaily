/*
    1st: hashtable

    Time    O(N)
    Space   O(N)
    2577 ms, faster than 63.42%
*/
var findWinners = function(matches) {
    const playersHistory = {} // { player: [win, lose]}
    for (let [winner, loser] of matches) {
        if (winner in playersHistory == false) {
            playersHistory[winner] = [0, 0]
        }
        playersHistory[winner][0] += 1
        if (loser in playersHistory == false) {
            playersHistory[loser] = [0, 0]
        }
        playersHistory[loser][1] += 1
    }
    const allwins = []
    const lostOnces = []
    for (let p in playersHistory) {
        const [win, lose] = playersHistory[p]
        if (lose == 0) {
            allwins.push(p)
        } else if (lose == 1) {
            lostOnces.push(p)
        }
    }
    return [allwins, lostOnces]
};