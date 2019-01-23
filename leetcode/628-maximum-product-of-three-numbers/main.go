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
	Time		O(nlogn)
	Space		O(1)
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

/*
	2nd approach
	- find out the top 3 items and the bottom 2 items in the arr
	- compare top1 * top2 * top3 and top1 * bot1 * bot2
	Time		O(n)
	Space		O(1)
	44ms beats 100%
	23jan2019
*/
func maximumProduct1(nums []int) int {
	top1, top2, top3 := -1001, -1001, -1001
	bot1, bot2 := 1001, 1001

	for _, num := range nums {
		if num > top1 {
			top3 = top2
			top2 = top1
			top1 = num
		} else if num > top2 {
			top3 = top2
			top2 = num
		} else if num > top3 {
			top3 = num
		}

		if num < bot1 {
			bot2 = bot1
			bot1 = num
		} else if num < bot2 {
			bot2 = num
		}
	}

	a := top1 * top2 * top3
	b := top1 * bot1 * bot2
	if a > b {
		return a
	}
	return b
}

func main() {

}
