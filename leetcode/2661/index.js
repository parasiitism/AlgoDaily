/*
    hashtable
    - since the cell values are unique, we can use them as keys to store the cell coordinates
    - for every query, lookup the coordinate from the hashtable, and then decrement the 'capacity' of its i and j

    Time    O(RC)
    Space   O(RC)
*/
var firstCompleteIndex = function(arr, mat) {
    const R = mat.length
    const C = mat[0].length
    const ht = {}
    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            const v = mat[i][j]
            ht[v] = [i, j]
        }
    }
    const capacity_rows = Array(R).fill(C)
    const capacity_cols = Array(C).fill(R)
    for (let i = 0; i < arr.length; i++) {
        const x = arr[i]
        const [r, c] = ht[x]
        capacity_rows[r] -= 1
        capacity_cols[c] -= 1
        if (capacity_rows[r] === 0 || capacity_cols[c] === 0) {
            return i
        }
    }
    return -1
};