var promiseAllSettled = function(functions) {
    const n = functions.length
    return new Promise((resolve, reject) => {
        if (n == 0) {
            return resolve([])
        }
        const results = Array(n).fill(null)
        let cnt = 0
        functions.forEach(async (fn, idx) => {
            try {
                const result = await fn();
                results[idx] = { status: 'fulfilled', value: result }
            } catch (error) {
                results[idx] = { status: 'rejected', reason: error };
            } finally {
                cnt += 1
                if (cnt == n) {
                    resolve(results)
                }
            }
        })
    })
};