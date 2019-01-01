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
// https://www.algorithmsandme.com/find-kth-smallest-element-in-two-sorted-arrays/
// but the implementation is buggy
/*
func findKth2(a []int, b []int, k int) int {
	lenA := len(a)
	lenB := len(b)

	if lenA+lenB < k {
		return -1
	}

	iMin := 0
	iMax := lenA - 1
	if k-2 < lenA {
		iMax = k - 2
	}
	fmt.Println(iMin, iMax)

	i := 0
	j := 0

	for iMin <= iMax {
		i = (iMin + iMax) / 2
		j = k - 2 - i // i+j=k-2 since arrays start from 0
		fmt.Println(i, j)
		if j > 0 && b[j-1] > a[i] {
			// i is too small, must increase it
			iMin = i + 1
		} else if i > 0 && a[i-1] > b[j] {
			// i is too big, must decrease it
			iMax = i - 1
		} else {
			// i is perfect
			if a[i] > b[j] {
				return a[i]
			}
			return b[j]
		}
	}
	fmt.Println(iMin, iMax)
	return -1
}
*/
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
