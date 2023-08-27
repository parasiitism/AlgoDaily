/*
    hashtable
    - be careful of the corner cases: [], [1]

    Time    O(N)
    Space   O(N)
*/
var isGood = function(nums) {
    const n = nums.length
    if (n < 2) {
        return false
    }
    const ctr = {}
    for (let i = 0; i < n; i++) {
        if (nums[i] in ctr === false) {
            ctr[nums[i]] = 0
        }
        ctr[nums[i]] += 1
    }
    for (let x = 1; x < n; x++) {
        if (x < n-1) {
            if (ctr[x] !== 1) {
                return false
            }
        } else {
            if (ctr[x] != 2) {
                return false
            }
        }
    }
    return true
};