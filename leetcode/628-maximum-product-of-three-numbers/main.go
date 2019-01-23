package main

import "sort"

/*
	Questions to ask:
	- will the array length < 3?
	- will there be negative numbers?
*/

/*
	navie approah: brute force
	Time	O(n^3)
	not gonna implement
*/

/*
	1st approach
	- sort the arr, compare nums[0] * nums[1] * nums[-1] and nums[-3] * nums[-2] * nums[-1]
	76ms beats 28.57%
	23jan2019
*/
func maximumProduct(nums []int) int {
	sort.Ints(nums)
	a := nums[0] * nums[1] * nums[len(nums)-1]
	b := nums[len(nums)-3] * nums[len(nums)-2] * nums[len(nums)-1]
	if a > b {
		return a
	}
	return b
}

func main() {

}
