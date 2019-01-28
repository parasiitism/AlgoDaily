package main

import "fmt"

/*
	Questions to ask:
	- what if the array is empty?
	- for [1,99,999], 999, return 1? becos there is one subarray, which has only one item 999, add up to 999?
*/

/*
	1st approach: prefix sum
	Time O(n^2)
	Space O(n)
	TLE
*/

/*
	2nd approach:
	- learned from others: https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/discuss/77807/Clean-python-solution-one-pass
	- the basic idea is to store the previous sum in a hashtable
			e.g. key: previous sum, value: index of the previous sum
	- if currentSum - target in the hastable, the result is currentIndex - hastable[previous sum]
	Time O(n)
	Space O(n) hashtable
	24ms beats 100%
*/
func maxSubArrayLen(nums []int, k int) int {
	res := 0
	acc := 0
	ht := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		acc += nums[i]
		if acc == k {
			res = i + 1
		} else if _, x := ht[acc-k]; x {
			if i-ht[acc-k] > res {
				res = i - ht[acc-k]
			}
		}
		if _, x := ht[acc]; !x {
			ht[acc] = i
		}
	}
	return res
}

func main() {
	fmt.Println(maxSubArrayLen([]int{1, -1, 5, -2, 3}, 3))
	fmt.Println(maxSubArrayLen([]int{-2, -1, 2, 1}, 1))
	fmt.Println(maxSubArrayLen([]int{-2, -1, 2, 1, 100}, 100))
	fmt.Println(maxSubArrayLen([]int{-2, -1, 2, 100, 1}, 100))
	fmt.Println(maxSubArrayLen([]int{-2, -1, 2, 1000}, 99))
}
