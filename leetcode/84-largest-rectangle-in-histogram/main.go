package main

import "math"

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

func main() {

}
