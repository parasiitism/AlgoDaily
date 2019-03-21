package main

import (
	"fmt"
	"math"
)

/*
	1st approach: brute force
	- for each bar, calculate the height from the current index to the index 0

	Time	O(n^2)
	Space	O(1)
	484 ms, faster than 28.75%
*/
func largestRectangleArea(heights []int) int {
	res := 0
	for i := 0; i < len(heights); i++ {
		// max height when we go backward
		maxheight := math.MaxInt64
		cnt := 1
		for j := i; j >= 0; j-- {
			maxheight = findMin(maxheight, heights[j])
			temp := maxheight * cnt
			if temp > res {
				res = temp
			}
			cnt++
		}
	}
	return res
}

func findMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

/*
	2nd approach: stack <= learned from others
	- use a stack to store the indeces where the corresponding height can create a potential largest retangle

	ref:
	- https://www.youtube.com/watch?v=ZmnqCZp9bBs

	Time	O(n)
	Space	O(1)
	8 ms, faster than 100.00%
*/
func largestRectangleArea1(heights []int) int {
	res := 0
	if len(heights) == 0 {
		return 0
	}
	stack := []int{-1, 0}
	for i := 1; i < len(heights); i++ {
		cur := heights[i]
		for len(stack) > 1 && cur < heights[stack[len(stack)-1]] {
			idx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			temp := heights[idx] * (i - stack[len(stack)-1] - 1)
			if temp > res {
				res = temp
			}
		}
		stack = append(stack, i)
	}
	for len(stack) > 1 {
		idx := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		temp := heights[idx] * (len(heights) - stack[len(stack)-1] - 1)
		if temp > res {
			res = temp
		}
	}
	return res
}

func main() {
	fmt.Println(largestRectangleArea1([]int{2, 1, 5, 6, 2, 3}))
	fmt.Println(largestRectangleArea1([]int{12, 23, 12, 25, 3, 16}))
}
