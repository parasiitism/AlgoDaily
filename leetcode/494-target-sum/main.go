package main

import (
	"fmt"
)

// dfs iterative, beats 57.14%
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

func main() {
	fmt.Println(findTargetSumWays([]int{1, 1, 1, 1, 2}, 4))
}
