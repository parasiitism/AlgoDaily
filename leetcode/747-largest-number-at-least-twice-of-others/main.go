package main

import (
	"fmt"
	"sort"
)

/*
	question to ask:
	- empty array?
	- single-element array?

	1st approach:
	- sort the array
	- see if cop[len(cop)-1] >= cop[len(cop)-2]*2
	Time		O(nlogn)
	Space		O(n)
	15jan2019
*/
func dominantIndex(nums []int) int {
	if len(nums) == 0 {
		return -1
	}
	if len(nums) == 1 {
		return 0
	}
	cop := []int{}
	cop = append(cop, nums...)
	sort.Ints(cop)
	if cop[len(cop)-1] >= cop[len(cop)-2]*2 {
		for i := 0; i < len(nums); i++ {
			if nums[i] == cop[len(cop)-1] {
				return i
			}
		}
	}
	return -1
}

func main() {
	fmt.Println(dominantIndex([]int{}))
	fmt.Println(dominantIndex([]int{1}))
	fmt.Println(dominantIndex([]int{1, 3, 2, 6, 0}))
	fmt.Println(dominantIndex([]int{1, 3, 3, 6, 0}))
	fmt.Println(dominantIndex([]int{1, 3, 6, 6, 0}))
	fmt.Println(dominantIndex([]int{1, 3, 2, 4}))
}
