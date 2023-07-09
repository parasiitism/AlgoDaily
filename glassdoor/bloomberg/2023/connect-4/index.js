/*
    Given a game board of Connect4, check current status and return
    - who wins without any moves
    - one of the players can win with the next move. The input is board(2D array), and the next player.

    e.g.1
    [
        'XXXXXXX',
        'XXXXRXX',
        'XXYYYXX',
        'XXRYYXX',
        'XYRRYRX',
        'XRYRRYR',
    ]
    output: ['Y']

    e.g.2
    [
        'XXXXXXX',
        'XXYXXXX',
        'XXYXXXX',
        'XXYXRRX',
        'XRRXYRY',
        'RYYRYRY',
    ]
    output: ['Y','R']

    ref:
    - https://leetcode.com/discuss/interview-question/3132448/Bloomberg-Phone-Screen-question
*/
const willWin = board => {
    const R = board.length
    const C = board[0].length
    const B = []
    for (let i = 0; i < R; i++) {
        const row = []
        for (let j = 0; j < C; j++) {
            row.push(board[i][j])
        }
        B.push(row)
    }
    // check current
    const winner = check(B)
    if (winner != null) {
        return [winner]
    }
    // check add 1 move
    const winners = new Set()
    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            if (B[i][j] === 'X' && i+1 < R && B[i+1][j] !== 'X') {
                // test if we put Red
                B[i][j] = 'R'
                if (check(B) != null) {
                    winners.add('R')
                }
                // test if we put Yellow
                B[i][j] = 'Y'
                if (check(B) != null) {
                    winners.add('Y')
                }
                // backtrack
                B[i][j] = 'X'
            }
        }
    }
    return Array.from(winners)
}

const check = B => {
    const R = B.length
    const C = B[0].length
    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            if (B[i][j] === 'X') {
                continue
            }
            // check to the right
            let _j = j
            while (_j+1 < C && B[i][_j] == B[i][_j+1]) {
                _j += 1
            }
            if (_j - j + 1 >= 4) {
                return B[i][j]
            }
            // check to the right
            let _i = i
            while (_i+1 < R && B[_i][j] == B[_i+1][j]) {
                _i += 1
            }
            if (_i - i + 1 >= 4) {
                return B[i][j]
            }
            // check to the bottom-right
            _i = i
            _j = j
            while (_i+1 < R && _j+1 < C && B[_i][_j] == B[_i+1][_j+1]) {
                _i += 1
                _j += 1
            }
            if (_i - i + 1 >= 4) {
                return B[i][j]
            }
            // check to the bottom-left
            _i = i
            _j = j
            while (_i+1 < R && _j-1 >= 0 && B[_i][_j] == B[_i+1][_j-1]) {
                _i += 1
                _j -= 1
            }
            if (Math.abs(_i - i + 1) >= 4) {
                return B[i][j]
            }
        }
    }

    return null
}

let a = [
    'XXXXXXX',
    'XXXXRXX',
    'XXYYYXX',
    'XXRYYXX',
    'XYRRYRX',
    'XRYRRYR',
]
console.log(willWin(a))

a = [
    'XXXXXXX',
    'XXYXXXX',
    'XXYXXXX',
    'XXYXRRX',
    'XRRXYRY',
    'RYYRYRY',
]
console.log(willWin(a))