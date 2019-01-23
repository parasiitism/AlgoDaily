/*
  1st approach
  - itereate once, use splice to remove the target
  Time  O(n)
  Space O(1)
  72ms beats 14.82
  23jan2019
*/
var removeElement = function (nums, val) {
  let i = 0
  while (i < nums.length) {
    if (nums[i] == val) {
      nums.splice(i, 1)
    } else {
      i++
    }
  }
  return nums.length
};

/*
  2nd approach
  - 2 pointers
  - itereate once, if the slow pointer == val, swap the element to the rigth
  Time  O(n)
  Space O(1)
  72ms beats 14.82
  23jan2019
*/
var removeElement = function (nums, val) {
  let i = 0
  let j = 0
  while (j < nums.length) {
    if (nums[i] != val) {
      i++
    } else if (nums[j] != val) {
      const temp = nums[i]
      nums[i] = nums[j]
      nums[j] = temp
      i++
    }
    j++
  }
  return i
};

let a = [3, 2, 2, 3]
console.log(removeElement(a, 2))
console.log(a)

a = [0, 1, 2, 2, 3, 0, 4, 2]
console.log(removeElement(a, 2))
console.log(a)
