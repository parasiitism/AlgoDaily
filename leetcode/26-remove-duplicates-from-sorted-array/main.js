/*
  1st approach:
  - just pop the duplicate items
  - return the length
  Time    O(n)
  Space   O(1)
  108ms beats 47.87%
  21jan2019
*/
var removeDuplicates = function (nums) {
  if (nums.length == 0) {
    return 0
  }
  let cur = nums[0]
  let i = 1
  while (i < nums.length) {
    if (nums[i] == cur) {
      nums.splice(i, 1) // js splice is in-place
    } else {
      cur = nums[i]
      i += 1
    }
  }
  return nums.length
};

let a = []
console.log(removeDuplicates(a))
console.log(a)

a = [1]
console.log(removeDuplicates(a))
console.log(a)

a = [1, 1]
console.log(removeDuplicates(a))
console.log(a)

a = [1, 2]
console.log(removeDuplicates(a))
console.log(a)

a = [1, 1, 2]
console.log(removeDuplicates(a))
console.log(a)

a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
console.log(removeDuplicates(a))
console.log(a)


a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4]
console.log(removeDuplicates(a))
console.log(a)