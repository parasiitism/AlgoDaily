package main

import (
	"fmt"
	"math"
	"sort"
)

/*
⭐️ Basic but not easy. I was asked by a friend who works at a top startup

There was a sorted sequence from 1 to N, but then there is a number mistyped and the order of the sequence is messed-up.
Please find out the unique mistyped number in an unsorted array.

e.g.
originally,
array = [1, 2, 3, 4, 5, 6]

now,
input = [1, 3, 2, 5, 6, 3]

expct output: 3(u can also print out the missing one: 4)

Conditions:
1. the original sequence must start from 1
2. only one number is mistyped and guarentee that there must be a mistyed number
3. the mistyped number can be at any index in the array
4. the number of items in the array will be from 2 to 1000. (follow-up: from 2 to 1000000000)

*/

// approach 1
// naive: iterative for each
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

// approach 2
// less naive: binary search
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

// approach 3
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

// approach 4
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

// approach 5
// however,
// the above solution has a problem for a large number set e.g. N=10000000, x! will stackoverflow the int64
// therefore we should not use 'mutiply'
// lets say for [1, 2, 3, 3, 5, 6] what if we...
// a^2 + b^2 + c^2 + d^2 + e^2 + f^2 = 91
// 					minus both sides
// a^2 + b^2 + c^2 + c^2 + d^2 + f^2 = 84
// there will be an equation, e^2 - c^2 = 91-75 = 7
// e - c = 1
// e + c = 7
// c=3, e=4
func findMistyped_math_advanced(nums []int) int {
	p1 := 0
	p2 := 0
	s1 := 0
	s2 := 0
	// find original product and sum
	for i := 1; i <= len(nums); i++ {
		p1 += i * i
		s1 += i
	}
	// find current product and sum
	for i := 0; i < len(nums); i++ {
		p2 += nums[i] * nums[i]
		s2 += nums[i]
	}
	p_diff := p1 - p2
	s_diff := s1 - s2
	result := (p_diff/s_diff - s_diff) / 2
	return result
}

func main() {
	// expect 3
	fmt.Println(findMistyped_math([]int{1, 3, 2, 5, 6, 3}))
	// expect 6
	fmt.Println(findMistyped_math([]int{1, 6, 3, 4, 5, 6}))

	// expect 3
	fmt.Println(findMistyped_math_advanced([]int{1, 3, 2, 5, 6, 3}))
	// expect 6
	fmt.Println(findMistyped_math_advanced([]int{1, 6, 3, 4, 5, 6}))
}
