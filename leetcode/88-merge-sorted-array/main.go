package main

import (
	"fmt"
	"sort"
)

/*
	naive approach
	- replace the zeros with the nums2 items
	- sort the nums1
	Time	O(nlogn)
	Space	O(1)
	0ms, no beats
*/
func merge(nums1 []int, m int, nums2 []int, n int) {
	j := 0
	for i := 0; i < len(nums1); i++ {
		if nums1[i] == 0 && j < len(nums2) {
			nums1[i] = nums2[j]
			j++
		}
	}
	sort.Ints(nums1)
}

/*
	1nd approach: learned from others
	https://www.youtube.com/watch?v=rZ9lcXCWSUg / ./idea_from_byte_by_byte.mp4
	compress .mov to .mp4: ffmpeg -i idea_from_byte_by_byte.mov -vcodec libx264 -crf 20 output.mp4
	- 3 pointers
	- replace thr nums1 from backward with larger values iteratively
	Time	O(m+n)
	Space	O(1)
	0 ms, faster than 100.00%
*/
func merge1(nums1 []int, m int, nums2 []int, n int) {
	p1 := m - 1
	p2 := n - 1
	cur := len(nums1) - 1
	for p1 >= 0 && p2 >= 0 {
		if nums1[p1] > nums2[p2] {
			nums1[cur] = nums1[p1]
			cur--
			p1--
		} else {
			nums1[cur] = nums2[p2]
			cur--
			p2--
		}
	}
	// be careful:
	// it is possible that m is negative but there are still elements in the nums2
	// we should put all the items from the rest of the nums into nums1
	for p2 >= 0 {
		nums1[cur] = nums2[p2]
		cur--
		p2--
	}
	// if p2 == -1, it means that we have merged all the nums2 into nums2,
	// so we dont really need to check if p1 >= 0
}

func main() {
	a := []int{1, 2, 3, 0, 0, 0}
	b := []int{2, 5, 6}
	merge(a, 3, b, 3)
	fmt.Println(a)

	a = []int{0}
	b = []int{1}
	merge1(a, 0, b, 1)
	fmt.Println(a)
}
