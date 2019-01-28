package main

import "fmt"

/*
	Naive approach:
	- prefix sum
	TLE: same as leetcode 325
*/

/*
	1st approach
	- this question is fucking similar to leetcode 325
  - the basic idea is to store the previous sum in a hashtable
		e.g. key: previous sum, value: number of occurence of a previous sum
	- if currentSum - target in the hastable, the result+1
	Time	O(n)
	Space O(n)
	24ms beats 100%
	28jan2019
*/
func subarraySum(nums []int, k int) int {
	res := 0
	acc := 0
	// key: previous sum, value: number of occurence of a previous sum
	ht := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		acc += nums[i]
		if acc == k {
			res++
		}
		if _, x := ht[acc-k]; x {
			res += ht[acc-k]
		}
		if _, x := ht[acc]; !x {
			ht[acc] = 1
		} else {
			ht[acc]++
		}
	}
	return res
}

func main() {
	fmt.Println(subarraySum([]int{1, 1, 1}, 1))             // 2
	fmt.Println(subarraySum([]int{1, 1, 1}, 2))             // 3
	fmt.Println(subarraySum([]int{1, 1, 1}, 3))             // 1
	fmt.Println(subarraySum([]int{1, 1, 1, 1}, 3))          // 2
	fmt.Println(subarraySum([]int{1, -1, 5, -2, 3}, 3))     // 3
	fmt.Println(subarraySum([]int{-2, -1, 2, 1}, 1))        // 2
	fmt.Println(subarraySum([]int{-2, -1, 2, 1, 100}, 100)) // 2
	fmt.Println(subarraySum([]int{-2, -1, 2, 100, 1}, 100)) // 2
	fmt.Println(subarraySum([]int{-2, -1, 2, 1000}, 99))    // 0
}
