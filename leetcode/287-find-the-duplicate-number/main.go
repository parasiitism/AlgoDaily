package main

import (
	"fmt"
	"sort"
)

// hash table
// time: O(n)
// space: O(n)
func findDuplicate(nums []int) int {
	var hashtable = make(map[int]int)
	for i := 0; i < len(nums); i++ {
		x := nums[i]
		if hashtable[x] > 0 {
			return x
		} else {
			hashtable[x] = 1
		}
	}
	return -1
}

// sort
// time: O(nlongn)
// space: O(1)
// look for the duplicate adjacent items
func findDuplicate1(nums []int) int {
	if len(nums) <= 1 {
		return -1
	}
	sort.Ints(nums)
	for i := 1; i < len(nums); i++ {
		x := nums[i]
		y := nums[i-1]
		if x == y {
			return x
		}
	}
	return -1
}

// actually leetcode suggest a method called "Floyd's Tortoise and Hare (Cycle Detection)"
// i think it is good to know but this solution is the way too special

func main() {
	ans := findDuplicate([]int{1, 3, 4, 2, 2})
	fmt.Println(ans)
}
