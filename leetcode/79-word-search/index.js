/*
    1st: backtracking

    Time    O(N * 3^L) N: number of cells, L: length of target word, 3^L instead of 4^L because we dont go backward
    Space   O(N)
*/
var exist = function(board, word) {
    const R = board.length
    const C = board[0].length

    const backtracking = (i, j, idx) => {
        if (idx === word.length) {
            return true
        }
        if (i < 0 || i == R || j < 0 || j == C) {
            return false
        }
        if (board[i][j] !== word[idx]) {
            return false
        }
        const cache = board[i][j]
        board[i][j] = '#'
        const dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        for (let [di, dj] of dirs) {
            const _i = i+di
            const _j = j+dj
            if(backtracking(_i, _j, idx+1)) {
                return true
            }
        }
        board[i][j] = cache
        return false
    }

    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            if (board[i][j] === word[0]) {
                const b = backtracking(i, j, 0)
                if (b) {
                    return true
                }
            }
        }
    }
    return false
};

let a = [
	["A", "B", "C", "E"],
	["S", "F", "C", "S"],
	["A", "D", "E", "E"],
];
let b = "ABCCED";
console.log(exist(a, b));

b = "SEE";
console.log(exist(a, b));

b = "ABCB";
console.log(exist(a, b));

console.log("-----")

/*
    3rd: backtracking without mutating the array

    Time    O(N * 3^L) N: number of cells, L: length of target word, 3^L instead of 4^L because we dont go backward
    Space   O(N)
    348 ms, faster than 59.46%
*/
var exist = function(board, word) {
    const R = board.length
    const C = board[0].length
    const used = new Set()

    const backtracking = (x, y, idx) => {
        if (idx == word.length) {
            return true
        }
        if (x < 0 || x == R || y < 0 || y == C) {
            return false
        }
        if (board[x][y] !== word[idx]) {
            return false
        }
        const key = `${x},${y}`
        if (used.has(key)) {
            return false
        }
        used.add(key)
        const dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        for (let [di, dj] of dirs) {
            const i = x+di
            const j = y+dj
            if (backtracking(i, j, idx+1) === true) {
                return true
            }
        }
        used.delete(key)
        return false
    }

    for (let i = 0 ; i < R; i++) {
        for (let j = 0 ; j < C; j++) {
            if (board[i][j] == word[0]) {
                if (backtracking(i, j, 0)) {
                    return true
                }
            }
        }
    }
    return false
};