/*
    1st approach: sort
    - sort it, and then split them and put the numbers back to the array

    e.g. even
    [3,5,2,1,6,4] => [1,2,3,4,5,6]
    split => [1,2,3], [4,5,6]
    result will be [1,4,2,5,3,6]

    e.g. odd
    [3,5,2,1,6] => [1,2,3,5,6]
    split => [1,2,4], [5,6]
    result will be [1,5,2,6,4]

    e.g. duplicate
    [3,5,2,1,3] => [1,2,3,3,5]
    split => [1,2,3], [3,5]
    result will be [1,3,2,5,3]

    Time    O(nlogn)
    Space   O(n)
    104 ms, faster than 55.43% 
*/
var wiggleSort = function (nums) {
	var wiggleSort = function(nums) {
        const n = nums.length
        const A = [...nums]
        A.sort((a, b) => a - b)
        const h = Math.ceil(n/2)
        for (let i = 0; i < h; i++) {
            nums[2*i] = A[i]
            if (2*i+1 < n) {
                nums[2*i+1] = A[h+i]
            }
        }
    };
};

/*
    2nd approach: swapping
    - this is quite similar to wiggle sort checking

    Time    O(n)
    Space   O(1)
    88 ms, faster than 90.22%
*/
var wiggleSort = function (nums) {
	const n = nums.length;
	if (n == 0) {
		return [];
	}
	for (let i = 1; i < n; i++) {
		if (i % 2 == 0) {
			if (nums[i] > nums[i - 1]) {
				[nums[i], nums[i - 1]] = [nums[i - 1], nums[i]];
			}
		} else {
			if (nums[i] < nums[i - 1]) {
				[nums[i], nums[i - 1]] = [nums[i - 1], nums[i]];
			}
		}
	}
};
