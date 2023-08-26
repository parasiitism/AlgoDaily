var findRLEArray = function(encoded1, encoded2) {
    let i = 0
    let j = 0
    const res = []
    while (i < encoded1.length && j < encoded2.length) {
        const [v1, f1] = encoded1[i]
        const [v2, f2] = encoded2[j]
        const v = v1 * v2
        const f = Math.min(f1, f2)

        if (res.length > 0 && res[res.length-1][0] === v) {
            res[res.length-1][1] += f
        } else {
            res.push([v, f])
        }

        encoded1[i][1] -= f
        encoded2[j][1] -= f

        if (f1 - f <= 0) {
            i += 1
        }
        if (f2 - f <= 0) {
            j += 1
        }
    }
    return res
};