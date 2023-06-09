/*
    Case 1: all numbers are non-negative

    Time    O(N)
    Space   O(1)
*/
var subarraySumLessOrEqualThanK = function(nums, k) {
    let res = 0
    let j = 0
    let p = 1
    for (let i = 0; i < nums.length; i++) {
        const x = nums[i]
        p += x
        while (j <= i && p > k) {
            const left = nums[j]
            p -= left
            j += 1
        }
        res += i - j + 1
    }
    return res
};

let a = [2, 5, 6]
let b = 10
console.log(subarraySumLessOrEqualThanK(a, b))

a = [1, 11, 2, 3, 15]
b = 10
console.log(subarraySumLessOrEqualThanK(a, b))

a = [1, 11, 2, 3, 15]
b = 13
console.log(subarraySumLessOrEqualThanK(a, b))

a = [3, 0, 0, 1, 2]
b = 4
console.log(subarraySumLessOrEqualThanK(a, b))

console.log("-----")

/*
    Case 2: some numbers can be negative
    - approach1: maintain a shorted list
    - approach2: binary indexed tree
    - approach3: binary search tree

    Time    O(N)
    Space   O(N)
*/