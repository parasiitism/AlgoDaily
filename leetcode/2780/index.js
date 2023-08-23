/*
    1st: 2 array minmax
    - first going backward, store the dominant ele at every index
    - then going forward, check the current dominant and the backward dominant of next element 

    Time    O(2N)
    Space   O(N)

*/
var minimumIndex = function(nums) {
    const n = nums.length
    const backward = Array(n).fill(null)
    let freqs = {}
    let curDominant = null
    for (let i = n - 1; i >= 0; i--) {
        const x = nums[i]
        if (x in freqs === false) { freqs[x] = 0 }
        freqs[x] += 1
        if (freqs[x] * 2 > n - i) {
            backward[i] = x
            curDominant = x
        } else if (freqs[curDominant] * 2 > n - i){
            backward[i] = curDominant
        }
    }
    freqs = {}
    for (let i = 0; i < n-1; i++) {
        const x = nums[i]
        if (x in freqs === false) { freqs[x] = 0 }
        freqs[x] += 1
        if (freqs[x] * 2 > i+1 && backward[i+1] == x) {
            return i
        }
    }
    return -1
};