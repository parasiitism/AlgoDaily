/*
    sort + sliding window
    - we are finding a subsequence but not a subarray, so the order doesn't matter
    - we can just sort the array first, and the find the longest winder where all the nums[any] - nums[i] <= target

    learned from others
    - https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/solutions/3771308/java-c-python-sliding-window/

    Time    O(NlogN + N)
    Space   O(1)
*/
var maximumBeauty = function(nums, k) {
    nums.sort((a, b) => a - b)
    let j = 0
    let res = 0
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] - nums[j] > k*2) {
            j += 1
        }
        res = Math.max(res, i - j + 1)
    }
    return res
};