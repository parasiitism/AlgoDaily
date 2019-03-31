package main

import (
	"fmt"
	"sort"
)

/*
	1st approach: binary search for the sum less thaen target, e.g. x + y < target
	- for each pair, we look for the remain
	e.g. [1,2,3,4,5] 10
	for pair 1,2, search for the value < 7 within [3,4,5]
	for pair 1,3, search for the value < 6 within [4,5]

	Time		O(n^2logn)
	Space		O(1)
	16 ms, faster than 18.18%
*/
func threeSumSmaller(nums []int, target int) int {
	if len(nums) < 3 {
		return 0
	}
	sort.Ints(nums)
	count := 0
	for i := 0; i < len(nums)-2; i++ {
		for j := i + 1; j < len(nums)-1; j++ {
			remain := target - nums[i] - nums[j]
			// find the lower bound
			temp := startingPositionBinarySearch(nums, remain, j+1)
			/*
				the index of target = lowerbound -1
				e.g. [1,3,5,5,5,7,9] find 5 => bsearch = 2
				therefore our target index is 2-1=1, which is 3
			*/
			k := temp - 1
			if k <= j {
				continue
			}
			count += k - j
		}
	}
	return count
}

func startingPositionBinarySearch(arr []int, target int, from int) int {
	min := from
	max := len(arr)
	for min < max {
		mean := (min + max) / 2
		if target <= arr[mean] {
			max = mean
		} else {
			min = mean + 1
		}
	}
	return min
}

/*
	2nd approach: 2 pointers
	- e.g. [2,3,6,10], 10
	pair=0,3, sum = 12, diff=+2, right--
	pair=0,2, sum = 8, diff=-2, left++ => count++
	pair=1,2, sum = 9, diff=-1, cannot move any pointers => count++
	...

	Time		O(n^2)
	Space		O(1)
	4 ms, faster than 100.00%
*/
func threeSumSmaller1(nums []int, target int) int {
	if len(nums) < 3 {
		return 0
	}
	sort.Ints(nums)
	count := 0
	for i := 0; i < len(nums)-2; i++ {
		left := i + 1
		right := len(nums) - 1
		for left < right {
			sum := nums[left] + nums[right] + nums[i]
			if sum >= target {
				right--
			} else {
				// this is the key
				// the diff: right - left is the pair that might help sum upto target with nums[i]
				count += right - left
				left++
			}
		}
	}
	return count
}

func main() {
	fmt.Println(threeSumSmaller([]int{-2, 0, 1, 3}, 2))
	fmt.Println(threeSumSmaller([]int{-2, 0, 1, 3, 4}, 3))
	fmt.Println("------------------------------")
	fmt.Println(threeSumSmaller1([]int{-2, 0, 1, 3}, 2))
	fmt.Println(threeSumSmaller1([]int{-2, 0, 1, 3, 4}, 3))
}
