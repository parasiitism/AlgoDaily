var findLeastNumOfUniqueInts = function(arr, k) {
    const ctr = {}
    for (let x of arr) {
        if (x in ctr === false) {
            ctr[x] = 0
        }
        ctr[x] += 1
    }
    const A = []
    for (let key in ctr) {
        A.push([ctr[key], key])
    }
    // console.log(ctr)
    A.sort((a, b) => a[0] - b[0])
    for (let i = 0; i < A.length; i++) {
        const [cnt, key] = A[i]
        if (k >= cnt) {
            delete ctr[key]
            k -= cnt
        } else if (k > 0) {
            ctr[key] -= k
            k = 0
        } else {
            break
        }
    }
    // console.log(ctr)
    return Object.keys(ctr).length
};