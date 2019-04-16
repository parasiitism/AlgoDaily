package main

// naive solution
// merge 2 arrays into one array and use builtin sort against the merged array
// return merged[k-1]
// Time 	O(nlogn)
// Space	O(m+n)
// i am not gonna implement it

/*
	2nd approach: 2 pointers to merge the arrays like merge sort
	- use 2 pointers to merge the arrays and return merged[half] or (merged[half-1]+merged[half])/2

	Time		O(m+n)
	Space 	O(m+n)
	24 ms, faster than 54.03%
*/
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	if len(nums1) == 0 && len(nums2) == 0 {
		return 0.0
	}
	len1, len2 := len(nums1), len(nums2)
	i, j := 0, 0
	merged := []int{}
	for i < len1 && j < len2 {
		if nums1[i] < nums2[j] {
			merged = append(merged, nums1[i])
			i++
		} else {
			merged = append(merged, nums2[j])
			j++
		}
	}
	for i == len1 && j < len2 {
		merged = append(merged, nums2[j])
		j++
	}
	for j == len2 && i < len1 {
		merged = append(merged, nums1[i])
		i++
	}
	if len(merged)%2 == 0 {
		return float64(merged[len(merged)/2-1]+merged[len(merged)/2]) / 2.0
	}
	return float64(merged[len(merged)/2])
}

// the suggested solution use binary search but i don understand
// https://leetcode.com/articles/median-of-two-sorted-arrays/
// Time		O(log(n+m))
// Space 	O(1)

func main() {

}
