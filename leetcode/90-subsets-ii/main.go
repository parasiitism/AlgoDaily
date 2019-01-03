package main

import (
	"fmt"
	"sort"
)

/*
	Recursive DFS using hashtables to avoid duplicates, see ./idea.jpeg
	Method similar to what I did for Permutation II
	Time    O(2^n) worst
	Space   O(2^n) recursion
	beats   100%
*/
func subsetsWithDup(nums []int) [][]int {
	sort.Ints(nums)
	return dfs(nums, []int{})
}

func dfs(nums []int, path []int) [][]int {
	result := [][]int{}
	result = append(result, path)
	seen := make(map[int]bool)
	for i := 0; i < len(nums); i++ {
		if _, x := seen[nums[i]]; x {
			continue
		}
		seen[nums[i]] = true
		// copy items
		nextPath := []int{}
		nextPath = append(nextPath, path...)
		nextPath = append(nextPath, nums[i])
		result = append(result, dfs(nums[i+1:], nextPath)...)
	}
	return result
}

func main() {
	fmt.Println(subsetsWithDup([]int{1, 2, 2}))
	fmt.Println(subsetsWithDup([]int{1, 2, 2, 1, 3}))
}
