package main

import "fmt"

/*
	Recursive DFS, see ./idea.jpeg
	Time    O(2^n)
	Space   O(2^n) recursion
	beats 100%
*/
func subsets(nums []int) [][]int {
	return dfs(nums, []int{})
}

func dfs(nums []int, path []int) [][]int {
	result := [][]int{}
	result = append(result, path)
	for i := 0; i < len(nums); i++ {
		// copy items
		nextPath := []int{}
		nextPath = append(nextPath, path...)
		nextPath = append(nextPath, nums[i])
		result = append(result, dfs(nums[i+1:], nextPath)...)
	}
	return result
}

/*
	Iterative DFS, see ./idea.jpeg
	Time    O(2^n)
	Space   O(2^n) stack
	beats 100%
*/
func subsets1(nums []int) [][]int {
	result := [][]int{}
	stack := []Stack{}
	stack = append(stack, Stack{nums, []int{}})
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		arr := pop.Nums
		path := pop.Path
		result = append(result, path)
		for i := 0; i < len(arr); i++ {
			nextPath := []int{}
			nextPath = append(nextPath, path...)
			nextPath = append(nextPath, arr[i])
			stack = append(stack, Stack{arr[i+1:], nextPath})
		}
	}
	return result
}

type Stack struct {
	Nums []int
	Path []int
}

/*
	Iteratively append the next item to calculated items
	e.g. [1,2,3]
	[]
	[],[1]
	[],[1],[2],[1,2]
	[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]
	Time    O(2^n)
	Space   O(2^n)
	beats 	100%
*/
func subsets2(nums []int) [][]int {
	result := [][]int{[]int{}}
	for i := 0; i < len(nums); i++ {
		n := len(result)
		for j := 0; j < n; j++ {
			cop := []int{}
			cop = append(cop, result[j]...)
			cop = append(cop, nums[i])
			result = append(result, cop)
		}
	}
	return result
}

func main() {
	fmt.Println(subsets2([]int{1, 2, 3}))
}
