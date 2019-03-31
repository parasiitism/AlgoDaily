package main

import (
	"fmt"
	"math"
	"sort"
)

/*
	questions to ask:
	- will there be an input array which length < 3 ? yes
	- so what is supposed to be returned when size < 3? 0
*/

/*
	1st approach: binary search
	- for each pair, we look for the remain
	e.g. [1,2,3,4,5] 10
	for pair 1,2, search 7 within [3,4,5]
	for pair 1,3, search 6 within [4,5]

	Time		O(n^2logn)
	Space		O(1)
	20 ms, faster than 23.68%
*/
func threeSumClosest(nums []int, target int) int {
	if len(nums) < 3 {
		return 0
	}
	sort.Ints(nums)
	res := math.MinInt32
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums)-1; j++ {
			tempTarget := target - nums[i] - nums[j]
			k := bSearchNearest(nums, tempTarget, j+1)
			if findAbs(nums[i]+nums[j]+nums[k]-target) < findAbs(res-target) {
				res = nums[i] + nums[j] + nums[k]
			}
		}
	}
	return res
}

func bSearchNearest(arr []int, target int, from int) int {
	min := from
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
	// compare and find the idx of the nearest item
	if max < from {
		return from
	}
	if min > len(arr)-1 {
		return len(arr) - 1
	}
	if findAbs(target-arr[max]) < findAbs(target-arr[min]) {
		return max
	}
	return min
}

func findAbs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

/*
	2nd approach: 2 pointers
	- e.g. [2,3,6,10], 10
	pair=0,3, sum = 12, diff=+2, right--
	pair=0,2, sum = 8, diff=-2, left++
	pair=1,2, sum = 9, diff=-1, cannot move any pointers

	Time		O(n^2)
	Space		O(1)
	4 ms, faster than 100.00%
*/
func threeSumClosest1(nums []int, target int) int {
	if len(nums) < 3 {
		return 0
	}
	sort.Ints(nums)
	diff := math.MaxInt64
	res := math.MinInt32
	for i := 0; i < len(nums); i++ {
		left := i + 1
		right := len(nums) - 1
		for left < right {
			sum := nums[i] + nums[left] + nums[right]
			if sum < target {
				if target-sum < diff {
					res = sum
					diff = target - sum
				}
				left++
			} else if sum > target {
				if sum-target < diff {
					res = sum
					diff = sum - target
				}
				right--
			} else {
				return sum
			}
		}
	}
	return res
}

func main() {
	fmt.Println(threeSumClosest([]int{0, 1, 2}, 3))
	fmt.Println(threeSumClosest([]int{-1, 2, 1, -4}, 1))
	fmt.Println(threeSumClosest([]int{-1, 2, 1, -4, 3}, 1))
	fmt.Println("----------------------------------------")
	fmt.Println(threeSumClosest([]int{0, 1, 2}, 3))
	fmt.Println(threeSumClosest([]int{-1, 2, 1, -4}, 1))
	fmt.Println(threeSumClosest([]int{-1, 2, 1, -4, 3}, 1))
}
