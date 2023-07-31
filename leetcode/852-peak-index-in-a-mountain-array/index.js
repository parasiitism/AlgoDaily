/*
    1st: 2 arrays

    Time    O(3N)
    Space   O(2N)
    120 ms, faster than 6.26%
*/
var peakIndexInMountainArray = function (A) {
	const n = A.length;

	const forwards = Array(n).fill(false);
	forwards[0] = true;
	for (let i = 1; i < n - 1; i++) {
		forwards[i] = A[i - 1] < A[i] && forwards[i - 1] === true;
	}

	const backwards = Array(n).fill(false);
	backwards[n - 1] = true;
	for (let i = n - 2; i >= 0; i--) {
		backwards[i] = A[i + 1] < A[i] && backwards[i + 1] === true;
	}

	for (let i = 1; i < n - 1; i++) {
		if (forwards[i] && backwards[i]) {
			return i;
		}
	}
};

/*
    same as lc162
*/
var peakIndexInMountainArray = function(nums) {
    let left = 0
    let right = nums.length-1
    while (left < right) {
        const mid = Math.floor((left + right) / 2)
        if (nums[mid] < nums[mid+1]) {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return left
};

/*
    2nd: upper boundy binary search
    - same as lc162

    Time    O(logN)
    Space   O(1)
    88 ms, faster than 11.15%
*/
var peakIndexInMountainArray = function(A) {
    let left = 0;
	let right = A.length - 1
    let res = 0
	while (left <= right) {
		const mid = Math.floor((left + right) / 2);
		if (A[mid] <= A[mid+1]) {
            left = mid + 1
        } else {
            res = mid
            right = mid - 1
        }
	}
	return res;
};
