package main

import "fmt"

/*
	1st approach
	- if not overlap, result = area A + area B
	- else, result = area A + area B - overlapping area
	use the method in leetcode 836 to determind if the rects overlap
	Time	O(1)
*/
func computeArea(A int, B int, C int, D int, E int, F int, G int, H int) int {
	if !isRectangleOverlap(A, B, C, D, E, F, G, H) {
		return (C-A)*(D-B) + (G-E)*(H-F)
	}
	x1 := max(A, E)
	y1 := max(B, F)
	x2 := min(C, G)
	y2 := min(D, H)
	return (C-A)*(D-B) + (G-E)*(H-F) - (x2-x1)*(y2-y1)
}

func isRectangleOverlap(A int, B int, C int, D int, E int, F int, G int, H int) bool {
	notOverlap := false
	if C <= E || A >= G {
		notOverlap = true
	}
	if D <= F || B >= H {
		notOverlap = true
	}
	return !notOverlap
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	fmt.Println(computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
	fmt.Println(computeArea(-2, -2, 2, 2, 1, -3, 3, -1))
}
