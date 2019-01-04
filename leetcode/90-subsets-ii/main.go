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

/*
	Iteratively append the next item to calculated items with a constraint
	e.g. [1,2,2,3]
	[]
	[],[1]                                                                      <- len_of_distinct = 1 during computation
	[],[1],[2],[1,2]                                                            <- len_of_distinct = 2 during computation
	[],[1],[2],[1,2],[2,2],[1,2,2]                                              <- len_of_distinct = 2 during computation
	[],[1],[2],[1,2],[2,2],[1,2,2],[3],[1,3],[2,3],[1,2,3],[2,2,3],[1,2,2,3]    <- len_of_distinct = 6 during computation
	Time    O(2^n) the worst. the actaul time depends on the number of duplicates
	Space   O(1)
	beats   29.41%
	ref: https://leetcode.com/problems/subsets-ii/discuss/30145/Accepted-java-iterative-solution
*/
func subsetsWithDup1(nums []int) [][]int {
	sort.Ints(nums)
	result := [][]int{[]int{}}
	lenOfDistinct := 1
	for i := 0; i < len(nums); i++ {
		size := len(result)
		if i > 0 && nums[i] != nums[i-1] {
			lenOfDistinct = size
		}
		for j := size - lenOfDistinct; j < size; j++ {
			// copy items
			nextPath := []int{}
			nextPath = append(nextPath, result[j]...)
			nextPath = append(nextPath, nums[i])
			result = append(result, nextPath)
		}
	}
	return result
}

func main() {
	fmt.Println(subsetsWithDup([]int{1, 2, 2}))
	fmt.Println(subsetsWithDup([]int{1, 2, 2, 1, 3}))

	fmt.Println(subsetsWithDup1([]int{1, 2, 2}))
	fmt.Println(subsetsWithDup1([]int{1, 2, 2, 1, 3}))
}
