/*
    Need to careful of the problem statement

    Time    O(N)
    Space   O(1)
*/
var isWinner = function(player1, player2) {
    let a = 0
    let b = 0
    for (let i = 0; i < player1.length; i++) {
        if ((i-2 >= 0 && player1[i-2] >= 10) || (i-1 >= 0 && player1[i-1] >= 10)) {
            a += 2 * player1[i]
        } else {
            a += player1[i]
        }
        if ((i-2 >= 0 && player2[i-2] >= 10) || (i-1 >= 0 && player2[i-1] >= 10)) {
            b += 2 * player2[i]
        } else {
            b += player2[i]
        }
    }
    
    if (a > b) {
        return 1
    } else if (a < b) {
        return 2
    }
    return 0
};