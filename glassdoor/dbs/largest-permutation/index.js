/*
  Given a list of integer, return the largest number which can be made from them
  e.g.1
  [54, 546, 548, 60] => 6054854654

  e.g.2
  [1, 34, 3, 98, 9, 76, 45, 4] => 998764543431
*/

function largestPermutation(arr) {

  let res = 0

  const dfs = function (nums, prefix) {
    if (nums.length == 0) {
      res = Math.max(res, prefix)
    } else {
      for (let i = 0; i < nums.length; i++) {
        // s[:i] + s[i+1:]
        const left = nums.slice(0, i)
        const right = nums.slice(i + 1, nums.length)
        const newNums = left.concat(right)
        // count digits of current num
        let cnt = 0
        let temp = nums[i]
        while (temp > 0) {
          temp = Math.floor(temp / 10)
          cnt++
        }
        // [12, 456] => 12*10^3 + 456
        let haha = prefix * Math.pow(10, cnt)
        dfs(newNums, prefix * Math.pow(10, cnt) + nums[i])
      }
    }
  }

  dfs(arr, 0)

  return res
}

console.log(largestPermutation([54, 546, 548, 60]))
console.log(largestPermutation([1, 34, 3, 98, 9, 76, 45, 4]))

// for (let i = 0; i < 5; i++) {
//   console.log(i)
// }