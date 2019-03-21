package main

/*
	classic approach: dynamic programming + max area within a histogram(leetcode 84)

	e.g.
	[
		[1,0,1,0,0],
		[1,0,1,1,1],
		[1,1,1,1,1],
		[1,0,0,1,0],
	]

	for each row, we accumulate the ones on the grids on position in previous row and find the area of the current histogram
	[1,0,1,0,0] <- maxarea 1
	[2,0,2,1,1] <- maxarea 3
	[3,1,3,2,2] <- maxarea 6
	[4,0,0,3,0] <- maxarea 4

	therefore the answer is 6

	Time  O(n^2)
	Space O(n)
	0 ms, faster than 100.00%
*/
func maximalRectangle(matrix [][]byte) int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return 0
	}
	retange := []int{}
	res := 0
	for i := 0; i < len(matrix); i++ {
		if len(retange) == 0 {
			for j := 0; j < len(matrix[i]); j++ {
				if matrix[i][j] == '0' {
					retange = append(retange, 0)
				} else {
					retange = append(retange, 1)
				}
			}
		} else {
			for j := 0; j < len(retange); j++ {
				if matrix[i][j] == '0' {
					retange[j] = 0
				} else {
					retange[j]++
				}
			}
		}
		area := largestRectangleArea(retange)
		if area > res {
			res = area
		}
	}
	return res
}

func largestRectangleArea(heights []int) int {
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

}
