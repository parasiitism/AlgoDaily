package main

import (
	"fmt"
)

// naive approach
// find out all the permutations and return the next one of the input
// Time		O(n!)
// Space	O(n) the array to store the numbers of permutations
// not gonna implement

/*
	1st attempt

	similar to lc556

	1. find the pivot point
	2. find the FURTHEST number which is a bit larger than the pivot in 2nd half
	3. swap the pivot and the number
	4. sort the 2nd half
	see idea.png
	time 	O(n+n)
	space 	O(1)
	beats 100%
*/
func nextPermutation(nums []int) {
	// find the pivot
	pivot := -1
	for i := len(nums) - 2; i >= 0; i-- {
		if nums[i]-nums[i+1] < 0 {
			pivot = i
			break
		}
	}
	// if no pivot
	if pivot == -1 {
		reverseFromTo(nums, 0, len(nums)-1)
		return
	}
	// look for the furthest target(just a bit larger than the pivot) to swap
	target := pivot + 1
	for last := pivot + 1; last < len(nums); last++ {
		if nums[last]-nums[pivot] > 0 && nums[last]-nums[pivot] <= nums[target]-nums[pivot] {
			target = last
		}
	}
	// swap the pivot and target
	temp := nums[target]
	nums[target] = nums[pivot]
	nums[pivot] = temp
	// reverse the suffix instead of sort
	reverseFromTo(nums, pivot+1, len(nums)-1)
}

// inplace reversal
func reverseFromTo(nums []int, from int, to int) {
	if from >= to {
		return
	}
	for from < to {
		temp := nums[from]
		nums[from] = nums[to]
		nums[to] = temp
		from++
		to--
	}
}

/*
	suggested solution
	actually it does the same thing but it is more concise
	AND it searches for the target from the end such that it saves time to find the furthest
	time 	O(n+n)
	space 	O(1)
	ofcos it beats 100%
*/
func nextPermutation1(nums []int) {
	// find pivot
	pivot := len(nums) - 2
	for pivot >= 0 && nums[pivot] >= nums[pivot+1] {
		pivot--
	}
	// find the furthest target in 2nd half
	if pivot >= 0 {
		target := len(nums) - 1
		for target >= 0 && nums[target] <= nums[pivot] {
			target--
		}
		// swap the pivot and target
		swap(nums, pivot, target)
	}
	// reverse the 2nd half
	reverse(nums, pivot+1)
}

func swap(nums []int, i int, j int) {
	temp := nums[i]
	nums[i] = nums[j]
	nums[j] = temp
}

func reverse(nums []int, start int) {
	i, j := start, len(nums)-1
	for i < j {
		swap(nums, i, j)
		i++
		j--
	}
}

func main() {
	a := []int{1, 3, 4, 2}
	nextPermutation(a)
	fmt.Println(a)

	a = []int{1, 2, 3}
	nextPermutation(a)
	fmt.Println(a) // 132

	a = []int{3, 2, 1}
	nextPermutation(a)
	fmt.Println(a) // 123

	a = []int{1, 1, 5}
	nextPermutation(a)
	fmt.Println(a) //151

	a = []int{1, 3, 2}
	nextPermutation(a)
	fmt.Println(a) // 213

	a = []int{2, 3, 1, 3, 3}
	nextPermutation(a)
	fmt.Println(a) // 23313

	a = []int{4, 2, 0, 2, 3, 2, 0}
	nextPermutation(a)
	fmt.Println(a) // [4,2,0,3,0,2,2]
}
