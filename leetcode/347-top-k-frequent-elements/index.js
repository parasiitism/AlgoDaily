/*
    1st approach
    - count num: freq into a hashtable
    - put the hashtable key&value into a priority queue
    - the first k elements are the top k elements in the priority queue

    56 ms, faster than 99.52%
*/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const ctr = {};
    nums.forEach(x => {
        if (x in ctr === false) {
            ctr[x] = 0
        }
        ctr[x] += 1
    })
    const arr = [];
    for (let key in ctr) {
        arr.push([ctr[key], key]);
    }
    arr.sort((a, b) => b[0] - a[0]);
    const res = []
    const n = Math.min(arr.length, k)
    for (let i = 0; i < n; i++) {
        res.push(arr[i][1])
    }
    return res
};
