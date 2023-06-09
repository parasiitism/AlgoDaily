/*
    1st approach: 2 pointers
	- when the current product is >= target, substruct the items on the left hand side
	- in each iteration, count the subarray
	e.g.
	[10,5,2,6,4], 100
	for 10 => [10] = 1
	for 5 => [10,5], [5] = 2
	for 2 => [5,2], [2] = 2
	for 6 => [5,2,6], [2,6], [6] = 3
	for 4 => [2,6,4], [6,4], [4] = 3
	count = 1+2+2+3+3 = 11

	hence, for each iteration, res += i - slow + 1

    Time    O(n)
    Space   O(1)
*/
var numSubarrayProductLessThanK = function(nums, k) {
    let res = 0
    let j = 0
    let p = 1
    for (let i = 0; i < nums.length; i++) {
        const x = nums[i]
        p *= x
        while (j < i && p >= k) {
            const left = nums[j]
            p /= left
            j += 1
        }
        if (p < k) {
            res += i - j + 1
        }
    }
    return res
};