/*
    2nd approach: binary search

    Time    O(2logn)
    Space   O(1)
    204 ms, faster than 5.22%
*/

var searchRange = function (nums, target) {
	const left = lowerBsearch(nums, target);
	const right = upperBsearch(nums, target);
	if (left >= right) {
		return [-1, -1];
	}
	return [left, right - 1];
};

const lowerBsearch = (nums, target) => {
	let left = 0;
	let right = nums.length;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		if (target <= nums[mid]) {
			right = mid;
		} else {
			left = mid + 1;
		}
	}
	return left;
};

const upperBsearch = (nums, target) => {
	let left = 0;
	let right = nums.length;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		if (target >= nums[mid]) {
			left = mid + 1;
		} else {
			right = mid;
		}
	}
	return left;
};

/*
    another way of binary search
*/
var searchRange = function(nums, target) {
    const n = nums.length
    const left = lowerBsearch(nums, target)
    const right = upperBsearch(nums, target) - 1
    if (left < 0 || left >= n || right < 0 || right >= n) {
        return [-1,-1]
    }
    if (nums[left] !== target || nums[right] !== target) {
        return [-1,-1]
    }
    return [left, right]
};

const lowerBsearch = (A, target) => {
    let left = 0
    let right = A.length - 1
    let res = A.length
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        if (target <= A[mid]) {
            res = mid
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    return res
}

const upperBsearch = (A, target) => {
    let left = 0
    let right = A.length - 1
    let res = A.length
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        if (target >= A[mid]) {
            left = mid + 1
        } else {
            res = mid
            right = mid - 1
        }
    }
    return res
}