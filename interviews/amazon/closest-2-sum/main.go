package main

import (
	"fmt"
	"sort"
)

/*
	naive approach
	- brute force
	Time	O(n^2)
	Space	O(1)
	not gonna implement
*/

/*
	better approach
	1. sort
	2. iterate the sorted from the back if sum > maxCap, else iterate from the front
	Time	O(n^2)
	Space	O(1)
	not gonna implement
*/
func closest2sum(nums []int, maxCap int) (int, int, int) {
	sort.Ints(nums)
	i, j := 0, len(nums)-1
	res := 0
	first, second := -1, -1
	for i < j {
		total := nums[i] + nums[j]
		if total > res && total <= maxCap {
			first = nums[i]
			second = nums[j]
			res = total
		}
		if total > maxCap {
			j--
		} else {
			i++
		}
	}
	return first, second, res
}

func main() {
	fmt.Println(closest2sum([]int{2, 4, 10, 11, 6, 5, 9}, 12))
	fmt.Println(closest2sum([]int{2, 4, 10, 11, 6, 5, 9}, 22))
	fmt.Println(closest2sum([]int{2, 4, 10, 11, 6, 6, 9}, 12))
	fmt.Println(closest2sum([]int{2, 4, 10, 11, 6, 5, 9}, 2))
	fmt.Println(closest2sum([]int{2, 4, 10, 11, 6, 5, 9}, 1))
}
