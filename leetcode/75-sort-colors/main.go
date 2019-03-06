package main

import "fmt"

/*
	questions to ask:
	- only 0,1,2? yes
*/

/*
	0th approach: merge sort

	Time	O(nlogn)
	Space	O(n)
	0 ms, faster than 100.00%
*/
func sortColors0(nums []int) {
	temp := mergeSort(nums)
	for i := 0; i < len(nums); i++ {
		nums[i] = temp[i]
	}
}

func mergeSort(nums []int) []int {
	// divide
	if len(nums) == 1 {
		return nums
	}
	mean := len(nums) / 2
	arr1 := mergeSort(nums[:mean])
	arr2 := mergeSort(nums[mean:])
	// merge 2 sorted arrays
	i, j := 0, 0
	result := []int{}
	for i < len(arr1) && j < len(arr2) {
		if arr1[i] < arr2[j] {
			result = append(result, arr1[i])
			i++
		} else {
			result = append(result, arr2[j])
			j++
		}
	}
	if i < len(arr1) {
		result = append(result, arr1[i:]...)
	}
	if j < len(arr2) {
		result = append(result, arr2[j:]...)
	}
	return result
}

/*
	1st approach: bucket sort

	Time	O(n)
	Space	O(3)
	0 ms, faster than 100.00%
*/
func sortColors(nums []int) {
	bucket := []int{0, 0, 0}
	for _, num := range nums {
		bucket[num]++
	}
	index := 0
	for i := 0; i < len(bucket); i++ {
		if bucket[i] > 0 {
			for j := 0; j < bucket[i]; j++ {
				nums[index] = i
				index++
			}
		}
	}
}

/*
	2nd approach:
	- move the zeros to the front
	- move the twos to the back
	- see leetcode 283) moving zeros

	Time	O(n)
	Space	O(2)
	0 ms, faster than 100.00%
*/
func sortColors1(nums []int) {
	idx0 := -1
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			nums[idx0+1], nums[i] = nums[i], nums[idx0+1]
			idx0++
		}
	}
	idx2 := len(nums)
	for i := len(nums) - 1; i >= 0; i-- {
		if nums[i] == 2 {
			nums[idx2-1], nums[i] = nums[i], nums[idx2-1]
			idx2--
		}
	}
}

/*
	3rd approach: suggested solution
	- the basic idea is 3 pointers partitioning the array into 3 parts and swap
	- https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation
	- https://en.wikipedia.org/wiki/Dutch_national_flag_problem

	iterations:
	[1 0 1 2 0 2]
	[1 0 1 2 0 2]
	[0 1 1 2 0 2]
	[0 1 1 2 0 2]
	[0 1 1 0 2 2]
	[0 0 1 1 2 2]
	[0 0 1 1 2 2]

	Time	O(d)
	Space	O(1)
	0 ms, faster than 100.00%
*/
func sortColors2(nums []int) {
	zero := 0
	one := 0
	two := len(nums) - 1
	for one <= two {
		if nums[one] == 0 {
			nums[zero], nums[one] = nums[one], nums[zero]
			zero++
			one++
		} else if nums[one] == 1 {
			one++
		} else {
			nums[one], nums[two] = nums[two], nums[one]
			two--
		}
	}
}

func main() {
	a := []int{2, 0, 1, 2, 0, 1}
	sortColors2(a)
	fmt.Println(a)

	a = []int{}
	sortColors(a)
	fmt.Println(a)

	a = []int{1, 2, 1}
	sortColors(a)
	fmt.Println(a)
}
