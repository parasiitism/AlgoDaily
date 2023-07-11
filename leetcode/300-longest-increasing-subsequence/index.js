/*
    1st approach: dynamic programming
    - similar to lc354, 646

    ref: Longest Increasing Subsequence
    - https://www.youtube.com/watch?v=CE2b_-XfVDk

    Time    O(n^2)
    Space   O(n)
    96 ms, faster than 55.81%
*/
var lengthOfLIS = function (nums) {
	if (nums.length == 0) {
        return 0
    }
    const n = nums.length
    const dp = Array(n).fill(1)
    for (let i = 0; i < n; i++) {
        let maxCount = 0
        for (let j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                maxCount = Math.max(maxCount, dp[j])
            }
        }
        dp[i] += maxCount
    }
    return Math.max(...dp)
};

let a;
a = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35];
console.log(lengthOfLIS(a));

/*
    follow up: print the subsequence
*/
var printLIS = function (nums) {
	const n = nums.length;
	const dp = [];
	for (let i = 0; i < n; i++) {
		dp.push([nums[i]]);
	}
	for (let i = 0; i < n; i++) {
		for (let j = 0; j < i; j++) {
			if (nums[j] < nums[i]) {
				if (dp[j].length + 1 > dp[i].length) {
					dp[i] = [...dp[j], nums[i]];
				}
			}
		}
	}
	console.log(dp);
	let res = [];
	for (let i = 0; i < n; i++) {
		if (dp[i].length > res.length) {
			res = dp[i];
		}
	}
	return res;
};

a = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35];
console.log(printLIS(a));

/*
    2nd: binary search
    - we are gonna maintain a sorted array A
        - A[i] represent the end of an increasing subsequence
        - i + 1 represent the length of that increasing subsequence
    1. when there is a larger number coming in, append it to A
    2. when there is a smaller number comming in, use it to replace a number in A

    e.g [100, 9, 2, 9, 3, 7, 101, 6].

    dp = [100]
    dp = [9]
    dp = [2]
    dp = [2, 9]
    dp = [2, 3]
    dp = [2, 3, 7]
    dp = [2, 3, 7, 101]
    dp = [2, 3, 6, 101]
                ^
                binary search 6, since 7 > 6, replace 7 with 6
    
    At the end,
    idx0 = 2,   means there is a subsequnce of length 1, which ends at 2. e.g. sub = [2]
    idx1 = 3,   means there is a subsequnce of length 2, which ends at 3. e.g. sub = [2, 3]
    idx2 = 6,   means there is a subsequnce of length 3, which ends at 6. e.g. sub = [2, 3, 6]
    idx3 = 101, means there is a subsequnce of length 4, which ends at 101. e.g. sub = [2, 3, 7, 101]

    ref:
    - https://leetcode.com/problems/longest-increasing-subsequence/discuss/667975/Python-3-Lines-dp-with-binary-search-explained

    Time    O(NlogN)
    Space   O(N)
    53ms beats 98.76%
*/
var lengthOfLIS = function(nums) {
    if (nums.length == 0) {
        return 0
    }
    const sub = []
    for (let x of nums) {
        if (sub.length > 0 && x > sub[sub.length-1]) {
            sub.push(x)
        } else {
            const j = lowerBsearch(sub, x)
            sub[j] = x
        }
    }
    return sub.length
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