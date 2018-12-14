package main

import (
	"fmt"
	"math"
	"sort"
)

/*
There is a sorted sequence from 1 to N,
but there is a number mistyped and the order of the sequence is messed-up. \
Please find out the unique mistyped number in an unsorted array.

e.g.
originally,
a = [1, 2, 3, 4, 5, 6]

now,
a = [1, 3, 2, 5, 6, 3]

output: 3(u can also print out the missing one: 4)

conditions:
1. start from 1
2. only one number is mistyped
3. the mistyped number can be at any index in the array

*/

// naive
// O(n^2)
// space O(1)
// im not gonna test it
func find_mistyped_naive(nums []int) int {
	for i := 0; i < len(nums); i++ {
		for j := 0; j < len(nums); j++ {
			if i != j && nums[i] == nums[j] {
				return nums[i]
			}
		}
	}
	return -1
}

// a bit better
// 1: sort the array
// 2: binary search on each item
// O(nlogn)
// space O(1)
//
func find_mistyped_less_naive(nums []int) int {
	sort.Ints(nums)
	for i := 0; i < len(nums); i++ {
		ex := []int{}
		ex = append(ex, nums[0:i]...)
		ex = append(ex, nums[i+1:]...)
		fmt.Println(ex)
		tempIdx := binary_search(ex, nums[i])
		if tempIdx != -1 {
			return nums[tempIdx]
		}
	}
	return -1
}

func binary_search(arr []int, target int) int {
	min := 0
	max := len(arr) - 1
	for min <= max {
		mean := (min + max) / 2
		if target == arr[mean] {
			return mean
		} else if target > arr[mean] {
			min = mean + 1
		} else if target < arr[mean] {
			max = mean - 1
		}
	}
	return -1
}

// what i usually do for duplicates
// hashtable
// O(n)
// space O(n)
func findMistyped(nums []int) int {
	hash := make(map[int]bool)
	for i := 0; i < len(nums); i++ {
		curr := nums[i]
		_, e := hash[curr]
		if !e {
			hash[curr] = true
		} else {
			return curr
		}
	}
	return -1
}

// i figured it out just because i took the GRE recently
// math
// O(n)
// space O(1)
// originally, 	abcdef=720
// now, 				abcdcf=540
// and 					a+b+c+d+e+f=21
// now 					a+b+c+d+c+f=20
// so...
// e/c=720/540=4/3
// e-c=1
// solve the equation
// c=3, e=4
func findMistyped_math(nums []int) int {
	p1 := 1
	p2 := 1
	s1 := 0
	s2 := 0
	// find original product and sum
	for i := 1; i <= len(nums); i++ {
		p1 *= i
		s1 += i
	}
	// find current product and sum
	for i := 0; i < len(nums); i++ {
		p2 *= nums[i]
		s2 += nums[i]
	}
	a_divide_b := float64(p1) / float64(p2)
	a_minis_b := float64(s1 - s2)
	result := a_minis_b / (a_divide_b - 1)
	return int(math.Round(result))
}

func main() {
	// expect 3
	fmt.Println(findMistyped_math([]int{1, 3, 2, 5, 6, 3}))
	// expect 6
	fmt.Println(findMistyped_math([]int{1, 6, 3, 4, 5, 6}))
}
