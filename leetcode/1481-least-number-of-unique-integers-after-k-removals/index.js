var findLeastNumOfUniqueInts = function(arr, k) {
    const freqs = {}
    for (let x of arr) {
        freqs[x] = freqs[x] ? freqs[x]+1 : 1
    }
    const keys = Object.keys(freqs)
    keys.sort((a, b) => freqs[a] - freqs[b])
    for (let key of keys) {
        if (freqs[key] <= k) {
            k -= freqs[key]
            delete freqs[key]
        } else {
            freqs[key] -= k
            k = 0
        }
    }
    return Object.keys(freqs).length
};