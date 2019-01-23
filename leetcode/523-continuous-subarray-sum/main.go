package main

import "fmt"

/*
	questions to ask:
	- will k be 0?
	- so of the sum == 0, k=any numer, return true?
	- will be be negative?
	- "continuous" means at least two ?
	- what if nums = [0,0] k = 0 ?
*/

/*
	1st approach
	- for each item, construct an array of sum, and return if sum%k == 0
		e.g.
		[23, 2, 4, 6, 7]
		23	25 29 35	42
				2		6	12	19
						4	10	13
							 6	 7
		^		^		^	 ^	 ^
	Time	O(n^2)
	Space	O(n(n+1)/2)
	104ms beats 0%
	15jan2019
*/
func checkSubarraySum1(nums []int, k int) bool {
	sumArr := [][]int64{}
	for i := 0; i < len(nums); i++ {
		sum := []int64{}
		if i > 0 {
			for j := 0; j < len(sumArr[i-1]); j++ {
				temp := sumArr[i-1][j] + int64(nums[i])
				if k != 0 && temp%int64(k) == 0 {
					return true
				} else if temp == 0 && k == 0 {
					return true
				}
				sum = append(sum, temp)
			}
		}
		sum = append(sum, int64(nums[i]))
		sumArr = append(sumArr, sum)
	}
	return false
}

/*
	2nd approach: optimize the above approach
	- actually we just need to compare the previuous arr and the current arr, so we can use 1d array instead of 2d
	Time	O(n^2)
	Space	O(n(n+1)/2)
	92ms beats 33.33%
	15jan2019
*/
func checkSubarraySum(nums []int, k int) bool {
	sumArr := []int64{}
	for i := 0; i < len(nums); i++ {
		sum := []int64{}
		for j := 0; j < len(sumArr); j++ {
			temp := sumArr[j] + int64(nums[i])
			if k != 0 && temp%int64(k) == 0 {
				return true
			} else if temp == 0 && k == 0 {
				return true
			}
			sum = append(sum, temp)
		}
		sum = append(sum, int64(nums[i]))
		sumArr = sum
	}
	return false
}

func main() {
	fmt.Println(checkSubarraySum([]int{0}, 0))              // false
	fmt.Println(checkSubarraySum([]int{0, 0}, -1))          // true
	fmt.Println(checkSubarraySum([]int{0, 0}, 0))           // true
	fmt.Println(checkSubarraySum([]int{0, 0}, 100))         // true
	fmt.Println(checkSubarraySum([]int{1, 5}, -6))          // true
	fmt.Println(checkSubarraySum([]int{5, 2, 4}, 5))        // false
	fmt.Println(checkSubarraySum([]int{23, 2, 4, 6, 7}, 6)) // true
	fmt.Println(checkSubarraySum([]int{23, 2, 6, 4, 7}, 6)) // true
}
