/*
    Recursion + Promise.all

    Time    O(n)
*/

/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Promise Function}
 */
const promisePool = async function(functions, n) {
    const worker = async () => {
        if (functions.length === 0) return;
        const fn = functions.shift();
        await fn();
        await worker();
    }
    const nPromises = []
    for (let i = 0; i < n; i++) {
        nPromises.push(worker())
    }
    return Promise.all(nPromises);
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */