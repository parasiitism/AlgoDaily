package main

import (
	"fmt"
)

// iterative dfs, beats 57.14%
type Stack struct {
	Depth int
	Sum   int
}

func findTargetSumWays(nums []int, S int) int {
	result := 0
	var stack []Stack
	stack = append(stack, Stack{-1, 0})
	for len(stack) > 0 {
		top := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		depth := top.Depth
		if depth == len(nums)-1 && top.Sum == S {
			result++
		}
		// next layer
		nextIdx := depth + 1
		if nextIdx < len(nums) {
			stack = append(stack, Stack{nextIdx, top.Sum + nums[nextIdx]})
			stack = append(stack, Stack{nextIdx, top.Sum - nums[nextIdx]})
		}
	}
	return result
}

// recursive dfs, beats 27.57%
func findTargetSumWays1(nums []int, S int) int {
	return dfs(nums, S, -1, 0, 0)
}

func dfs(nums []int, S int, depth int, sum int, result int) int {
	if len(nums) != 0 && depth == len(nums)-1 && sum == S {
		return result + 1
	}
	a := 0
	b := 0
	if depth+1 < len(nums) {
		a = dfs(nums, S, depth+1, sum+nums[depth+1], result)
		b = dfs(nums, S, depth+1, sum-nums[depth+1], result)
	}
	return a + b
}

func main() {
	a := []int{1, 1, 1, 1, 2}
	fmt.Println(findTargetSumWays(a, 4))
	fmt.Println(findTargetSumWays1(a, 4))
}
