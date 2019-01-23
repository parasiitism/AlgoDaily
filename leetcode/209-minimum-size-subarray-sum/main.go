package main

import (
	"fmt"
	"math"
)

/*
	questions to ask:
	- will there be no subarray add up to the s?
	- will there be negative?
	- will there be s=3, nums = [1,2,3], so the ans = 1?
	- let's say if s=0, nums = [0,0,0,0,0], the ans = 1?
*/

/*
	1st approach
	- store an array for each item, find the target in the subarray
	e.g.
  [23, 2, 4, 6, 7]
	23	25 29 35	42
			2		6	12	19
					4	10	13
							6	 7
	^		^		^	 ^	 ^
	if i-j+1 < res, res = i-j+1
	Time	O(n^2) n(n+1)/2
	Space O(n)
	2488 ms beats 5.8%
	23jan2019
*/
func minSubArrayLen(s int, nums []int) int {
	res := math.MaxInt64
	layer := []int{}
	for i := 0; i < len(nums); i++ {
		num := nums[i]
		temp := []int{}
		for j := 0; j < len(layer); j++ {
			x := layer[j] + num
			if x >= s && i-j+1 < res {
				res = i - j + 1
			}
			temp = append(temp, x)
		}
		if num >= s {
			res = 1
		}
		temp = append(temp, num)
		layer = temp
	}
	if res == math.MaxInt64 {
		return 0
	}
	return res
}

/*
	2nd approach
	- for each item, calculate from arr[i] to arr[j], if sum >= s and j-1+1<res, res = j - 1 + 1
	Time	O(n^2)
	Space O(1)
	2488 ms beats 20.29%
	23jan2019
*/
func minSubArrayLen1(s int, nums []int) int {
	res := math.MaxInt64
	for i := 0; i < len(nums); i++ {
		sum := 0
		for j := i; j < len(nums); j++ {
			sum += nums[j]
			if sum >= s {
				if j-i+1 < res {
					res = j - i + 1
				}
				break
			}
		}
	}
	if res == math.MaxInt64 {
		return 0
	}
	return res
}

func main() {
	fmt.Println(minSubArrayLen1(6, []int{2, 3, 1, 2, 4, 3}))
}
