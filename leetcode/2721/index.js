/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = async function(functions) {
    return new Promise((resolve, reject) => {
        const n = functions.length
        const res = Array(n).fill(null)
        let cnt = 0
        for (let i = 0; i < n; i++) {
            const f = functions[i]
            f().then(val => {
                res[i] = val
                cnt += 1

                if (cnt === n) {
                    resolve(res)
                }
            }).catch(error => reject(error))
        }
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */