/*
    https://leetcode.com/discuss/interview-question/407179/Bloomberg-or-Remove-array-elements-in-given-index-ranges

    Input: 
              0  1   2  3  4   5   6   7   8   9  10  11  12  13  14  15
    array = [-8, 3, -5, 1, 51, 56, 0, -5, 29, 43, 78, 75, 32, 76, 73, 76], 
    ranges = [[5, 8], [10, 13], [3, 6], [20, 25]]
    
    Output:
    [-8, 3, -5, 29, 43, 76, 73, 76]
*/
const removeItems = (nums, ranges) => {
    const intvs = mergeIntvs(ranges)
    console.log(intvs)
    const remain = []
    for (let i = 0; i < nums.length; i++) {
        const j = lowerBsearch(intvs, i)
        if (j >= 0 && j < intvs.length) {
            const [s, e] = intvs[j]
            if (s <= i && i <= e) {
                continue
            }
        }
        remain.push(nums[i])
    }
    return remain
}

const mergeIntvs = (intvs) => {
    intvs.sort((a, b) => a[0] - b[0])
    const res = []
    for (let [s, e] of intvs) {
        const n = res.length
        if (n > 0 && s <= res[n-1][1]) {
            res[n-1][1] = Math.max(res[n-1][1], e)
        } else {
            res.push([s, e])
        }
    }
    return res
}

const lowerBsearch = (intvs, target) => {
	let left = 0;
	let right = intvs.length
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		if (target <= intvs[mid][1]) {
            right = mid
        } else {
            left = mid + 1
        }
	}
	return left
};

let a, b

a = [-8, 3, -5, 1, 51, 56, 0, -5, 29, 43, 78, 75, 32, 76, 73, 76]
b = [[5, 8], [10, 13], [3, 6], [20, 25]]
console.log(removeItems(a, b))  // [-8, 3, -5, 29, 43, 76, 73, 76]