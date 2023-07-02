/*
    Case 1: all numbers are non-negative

    Time    O(N)
    Space   O(1)
*/
const longestSubarraySumLessThanOrEqualToK1 = function(nums, k) {
    let res = 0
    let j = 0
    let pfs = 0
    for (let i = 0; i < nums.length; i++) {
        const x = nums[i]
        pfs += x
        while (pfs > k) {
            const left = nums[j]
            pfs -= left
            j += 1
        }
        const sub_length  = i - j + 1
        res = Math.max(res, sub_length)
    }
    return res
};

let a = [2, 5, 6]
let b = 10
console.log(longestSubarraySumLessThanOrEqualToK1(a, b)) // 2 which is [2, 5]

a = [1, 11, 2, 3, 15]
b = 10
console.log(longestSubarraySumLessThanOrEqualToK1(a, b)) // 2 which is [2, 3]

a = [1, 11, 2, 3, 15]
b = 13
console.log(longestSubarraySumLessThanOrEqualToK1(a, b)) // 2 which is [1, 11]

a = [3, 0, 0, 1, 2]
b = 4
console.log(longestSubarraySumLessThanOrEqualToK1(a, b)) // 4 which is [3,0,0,1] or [0,0,1,2]

console.log("-----")

/*
    Case 2: some numbers can be negative

    Time    O(N)
    Space   O(N)
*/
const longestSubarraySumLessThanOrEqualToK2 = function(nums, k) {
    let res = 0
    let j = 0
    let pfs = 0
    for (let i = 0; i < nums.length; i++) {
        const x = nums[i]
        pfs += x
        while (pfs > k) {
            if (nums[j] < 0) {
                const left = nums[j]
                pfs -= left
            } else {
                const left = nums[j]
                pfs -= left
                j += 1
            }
        }
        const sub_length  = i - j + 1
        res = Math.max(res, sub_length)
    }
    return res
};

a = [2, 5, 6]
b = 10
console.log(longestSubarraySumLessThanOrEqualToK2(a, b)) // 2 which is [2, 5]

a = [1, 11, 2, 3, 15]
b = 10
console.log(longestSubarraySumLessThanOrEqualToK2(a, b)) // 2 which is [2, 3]

a = [1, 11, 2, 3, 15]
b = 13
console.log(longestSubarraySumLessThanOrEqualToK2(a, b)) // 2 which is [1, 11]

a = [3, 0, 0, 1, 2]
b = 4
console.log(longestSubarraySumLessThanOrEqualToK2(a, b)) // 4 which is [3,0,0,1] or [0,0,1,2]

a = [2, 5, -2, -1, 6]
b = 10
console.log(longestSubarraySumLessThanOrEqualToK2(a, b)) // 5 which is the whole array

a = [2, 5, -2, -1, 6, 6]
b = 10
console.log(longestSubarraySumLessThanOrEqualToK2(a, b)) // 5 which is [2, 5, -2, -1, 6, 6]