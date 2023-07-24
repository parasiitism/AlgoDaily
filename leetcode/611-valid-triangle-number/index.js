/*
    1st: binary search
    - sort the input array(nums)
    - a valid triangle can be identified when a + b > c
    - so for every pairs, binary search the upper bound for the third side of a triangle

    Time    O(N^2 * logN)
    Space   O(1)
    1500 ms, faster than 10.24%
*/
var triangleNumber = function(nums) {
    const n = nums.length
    nums.sort((a, b) => a - b)
    let res = 0
    for (let i = 0; i < n; i++) {
        for (let j = i+1; j < n; j++) {
            const k = lowerbsearch(nums, j+1, nums[i] + nums[j])
            res += k - 1 - j
        }
    }
    return res
};

const lowerbsearch = (A, start, target) => {
    let left = start
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

/*
    2nd: sort + 2 pointers
    - a + b > c
    - for every c, for the number of pairs which a + b > c
    
    Time    O(N^2 * logN)
    Space   O(1)
    1500 ms, faster than 10.24%
*/
var triangleNumber = function(A) {
    const n = A.length
    A.sort((a, b) => a - b)
    let res = 0
    for (let i = 2; i < n; i++) {
        let left = 0
        let right = i-1
        while (left < right) {
            if (A[left] + A[right] > A[i]) {
                left += 1
            } else {
                res += right - left // e.g. [2,2,2,2,3,4] => there are 4 pairs of [2,3]s we can combine with the [4] to make a triangle
                right -= 1
            }
        }
    }
    return res
};