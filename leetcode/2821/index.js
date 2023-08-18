/**
 * @param {Array<Function>} functions
 * @param {number} ms
 * @return {Array<Function>}
 */
var delayAll = function(functions, ms) {
    const res = []
    for (let f of functions) {
        res.push(() => new Promise((resolve, reject) => {
                setTimeout(() => {
                    f()
                    .then(result => resolve(result))
                    .catch(error => reject(error))
                }, ms)
            })
        )
    }
    return res
};