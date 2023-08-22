var invertObject = function(obj) {
    const res = {}
    for (let k in obj) {
        const v = obj[k]
        if (v in res) {
            if (!Array.isArray(res[v])) {
                res[v] = [res[v]]
            }
            res[v].push(k)
        } else {
            res[v] = k
        }
    }
    return res
};
