/*
    hashtable + sliding window
    
    crux:
    - for case e.g. [1, 3, 1, 2, 2] the slding window won't not cover the whole array
                     ^        ^
                        ^       ^
    but instead, when we do res += j, 
    meaning that all the subarrys which start from index0 to indexj-1 are already considered
*/
var countCompleteSubarrays = function(nums) {
    const uniques = new Set(nums)
    const ctr = new Map()
    let j = 0
    let res = 0
    for (let i = 0; i < nums.length; i++) {
        const right = nums[i]
        if (ctr.has(right) === false) {
            ctr.set(right, 0)
        }
        ctr.set(right, ctr.get(right) + 1)
        while (ctr.size == uniques.size) {
            const left = nums[j]
            ctr.set(left, ctr.get(left) - 1)
            if (ctr.get(left) == 0) {
                ctr.delete(left)
            }
            j += 1
        }
        res += j
    }
    return res
};