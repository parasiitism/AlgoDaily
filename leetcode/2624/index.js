/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    const res = []
    if (this.length != rowsCount * colsCount) {
        return res
    }
    for (let i = 0; i < rowsCount; i++) {
        res.push(Array(colsCount).fill(0))
    }

    for (let i = 0; i < this.length; i++) {
        let r = i % rowsCount
        const c = Math.floor(i / rowsCount)
        if (c%2 == 1) {
            r = rowsCount - r - 1
        }
        res[r][c] = this[i]
    }
    return res
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */