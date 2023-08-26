/*
    2nd approach: 2 pointers
	- fast pointer is the index of iteration
	- slow pointer is the index which indicates the nums[slow:fast+1] having valid count of zeros
	- learned from others: https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247543/O(n)-Java-Solution-using-sliding-window
	- see ./idea.jpeg

	Time	O(2n)
	Space	O(1)
	60 ms, faster than 100.00%
*/
var longestOnes = function(nums, k) {
    let j = 0
    let res = 0
    let zeros = 0
    for (let i = 0; i < nums.length; i++) {
        const right = nums[i]
        if (right === 0) {
            zeros += 1
        }
        while (zeros > k) {
            const left = nums[j]
            if (left === 0) {
                zeros -= 1
            }
            j += 1
        }
        res = Math.max(res, i - j + 1)
    }
    return res
};