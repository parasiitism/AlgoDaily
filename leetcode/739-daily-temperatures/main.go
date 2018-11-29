package main

import (
	"fmt"
)

// navie solution
// O(n^2) but still beats 41.54%
func dailyTemperatures_(T []int) []int {
	result := []int{}
	for i := 0; i < len(T); i++ {
		curr := T[i]
		found := false
		for j := i; j < len(T); j++ {
			if T[j] > curr {
				result = append(result, j-i)
				found = true
				break
			}
		}
		if !found {
			result = append(result, 0)
		}
	}
	return result
}

// better solution: stack
//  it beats 80%
// best complexity: O(n)
// worst complexity: > O(n). e.g. if the array is with humps, pop() operation is time consuming
type Stack struct {
	value int
	index int
}

func dailyTemperatures(T []int) []int {
	stack := []Stack{}
	result := make([]int, len(T))
	for i := len(T) - 1; i >= 0; i-- {
		curr := T[i]
		for len(stack) > 0 {
			top := stack[len(stack)-1]
			if top.value > curr {
				result[i] = top.index - i
				break
			}
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, Stack{curr, i})
	}
	return result
}

func main() {
	// g := []int{73, 73, 75, 71, 69, 72, 76, 73}
	// result := make([]int, len(g))
	// fmt.Println(result)
	fmt.Println(dailyTemperatures([]int{73, 73, 75, 71, 69, 72, 76, 73})) // expect [2 1 4 2 1 1 0 0]
}
