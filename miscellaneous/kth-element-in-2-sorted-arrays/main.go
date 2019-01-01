package main

import (
	"fmt"
	"sort"
)

// naive approach
// merge 2 arrays into one array and use builtin sort against the merged array
// return merged[k-1]
// Time 	O(nlogn)
// Space	O(m+n)
func findKth(a []int, b []int, k int) int {
	c := []int{}
	c = append(c, a...)
	c = append(c, b...)
	sort.Ints(c)
	return c[k-1]
}

// better approach
// use 2 pointers to merge the arrays and return merged[k-1] (classic question: merge 2 sorted arrays )
// Time		O(m+n)
// Space 	O(m+n)
func findKth1(a []int, b []int, k int) int {
	if len(a) == 0 && len(b) == 0 {
		return -1
	}
	lenA := len(a)
	lenB := len(b)
	i := 0
	j := 0
	merged := []int{}
	for i < lenA && j < lenB {
		if a[i] < b[j] {
			merged = append(merged, a[i])
			i++
		} else {
			merged = append(merged, b[j])
			j++
		}
	}
	if i == lenA {
		for j < lenB {
			merged = append(merged, b[j])
			j++
		}
	}
	if j == lenB {
		for i < lenA {
			merged = append(merged, a[i])
			i++
		}
	}
	return merged[k-1]
}

// so far the fastest solution
// binary search
// Time  O(logk)
// Space O(1)
// see main.py
// https://stackoverflow.com/questions/4607945/how-to-find-the-kth-smallest-element-in-the-union-of-two-sorted-arrays

func main() {

	// a := []int{1, 2, 3}
	// b := []int{4, 5, 6}

	// a := []int{4, 5, 6}
	// b := []int{1, 2, 3}

	// a := []int{1, 2, 3, 4, 5, 6}
	// b := []int{4, 5, 6, 7, 8, 9}

	// a := []int{1, 3, 5, 6, 7, 8, 9, 11}
	// b := []int{1, 4, 6, 8, 12, 14, 15, 17}

	// a := []int{1}
	// b := []int{4, 5, 6, 7, 8, 9}

	a := []int{4, 5, 6, 7, 8, 9}
	b := []int{1}

	fmt.Println(findKth1(a, b, 4))
}
