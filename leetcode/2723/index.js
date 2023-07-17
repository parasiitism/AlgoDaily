/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    let res = 0
    let cnt = 0
    const arr = [promise1, promise2]
    return new Promise((resolve, reject) => {
        for (let i = 0; i < arr.length; i++) {
            arr[i].then(data => {
                res += data
                cnt += 1
                if (cnt == arr.length) {
                    resolve(res)
                }
            }).catch(error => reject(error))
        }
    });
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */