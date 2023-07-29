/*
    2nd: sort + 2 pointers
    - optimize the 1st approach
    - we only care about the min and max in every subsequnce, it means that a sorted subsequence would help
    - for every LEGIT starting index, find out how many sequences whichs fulfills the condition
    - all subsequcens in an array = subsets = 2**N

    Time    O(NlogN + N)
    Space   O(1)
*/
var numSubseq = function(nums, target) {
    const MOD = 10**9 + 7
    const n = nums.length

    const pows = [1];
    for (let i = 1; i < nums.length; i++) {
        pows.push(pows[i - 1] * 2 % MOD);
    }

    nums.sort((a, b) => a - b)
    let left = 0
    let right = n - 1
    let res = 0
    while (left <= right) {
        if (nums[left] + nums[right] <= target) {
            res += pows[right - left]
            left += 1
        } else {
            right -= 1
        }
    }
    return res % MOD
};