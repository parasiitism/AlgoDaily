// [3,4,5,7], 7 => [0,1] index1, index2
// [3,4,5,7], 99 => [] index1, index2
function twoSum(nums, target) {
  const seen = {}
  for (let i = 0; i < nums.length; i++) {
    const remain = target - nums[i]
    if (seen[remain] !== undefined) {
      return [seen[remain], i]
    } else {
      seen[nums[i]] = i
    }
  }
  return []
}

// console.log(twoSum([3, 4, 5, 7], 7))
// console.log(twoSum([3, 4, 5, 7], 99))

// [2, 4, 10, 11, 6, 5, 9], 12 => [0, 2, 12] index1, index2, closest sum
// [3,4,5,7], 99 => [0, 3, 12] index1, index2, closest sum
function twoSumClosestInOneArray(nums, target) {
  nums.sort((a, b) => a - b)
  let i = 0
  let j = nums.length - 1
  let closest = nums[0] + nums[nums.length - 1]
  let targetI = 0
  let targetJ = nums.length - 1
  while (i < j) {
    const temp = nums[i] + nums[j]
    if (temp > closest && temp <= target) {
      closest = temp
      targetI = i
      targetJ = j
    }
    if (temp < target) {
      i++
    } else {
      j--
    }
  }
  return [targetI, targetJ, closest]
}

// console.log(twoSumClosestInOneArray([2, 4, 10, 11, 6, 5, 9], 12))
// console.log(twoSumClosestInOneArray([3, 4, 5, 7], 12))

/*
  Given 2 arrays of n integers, forwardRouteList and returnRouteList
  find the pair(s) in nums such that the sum is closest(<=) to a given number, target

  e.g.1
  target = 20
  nums1 = [[1, 8], [2, 7], [3, 14]]
  nums2 = [[1, 5], [2, 10], [3, 14]]
  return [[3, 1]] array of nums1 index, nums2 index

  e.g.2
  target = 20
  nums1 = [[1, 8], [2, 15], [3, 9]]
  nums2 = [[1, 8], [2, 11], [3, 12]]
  return [[1, 3], [3, 2]]
*/
function twoSumClosestInTwoArrays(nums1, nums2, target) {
  nums2.sort((a, b) => a[1] - b[1])
  let closest = 0
  const result = [[0, 0, closest]]
  for (let i = 0; i < nums1.length; i++) {
    const j = bsearch(nums2, target - nums1[i][1])
    if (j < 0) {
      continue
    }
    const temp = nums1[i][1] + nums2[j][1]
    if (temp > closest && temp < target) {
      closest = temp
      result[0] = [nums1[i][0], nums2[j][0], temp]
    } else if (temp == target) {
      if (closest < target) {
        result.pop()
      }
      closest = temp
      result.push([nums1[i][0], nums2[j][0], temp])
    }
  }
  return result
}

// binary search the num <= target
function bsearch(nums, target) {
  let left = 0
  let right = nums.length - 1
  while (left <= right) {
    const mean = Math.floor(Math.floor(left + right) / 2)
    if (nums[mean][1] == target) {
      return mean
    } else if (nums[mean][1] < target) {
      left = mean + 1
    } else {
      right = mean - 1
    }
  }
  return right
}

// return [ 1, 3, 20 ]
console.log(twoSumClosestInTwoArrays(
  [[1, 8], [2, 7], [3, 14]],
  [[1, 5], [2, 10], [3, 14]],
  20,
))

// return [[1, 3], [3, 2]]
console.log(twoSumClosestInTwoArrays(
  [[1, 8], [2, 15], [3, 9]],
  [[1, 8], [2, 11], [3, 12]],
  20
))