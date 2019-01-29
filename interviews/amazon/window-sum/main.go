package main

import "fmt"

func windowSum1(nums []int, k int) []int {
	if len(nums) == 0 || k <= 0 || k > len(nums) {
		return []int{}
	}
	res := []int{}
	acc := 0
	for i := 0; i < k; i++ {
		acc += nums[i]
	}
	res = append(res, acc)
	for i := k; i < len(nums); i++ {
		acc += nums[i]
		acc -= nums[i-k]
		res = append(res, acc)
	}
	return res
}

func windowSum2(nums []int, k int) [][]int {
	if len(nums) == 0 || k <= 0 || k > len(nums) {
		return [][]int{}
	}
	res := [][]int{}

	// first item
	temp := []int{}
	for i := 0; i < k; i++ {
		temp = append(temp, nums[i])
	}
	res = append(res, temp)

	// 2nd item -> end
	for i := k; i < len(nums); i++ {
		// [1,2,3] => [2,3,4] and put it into the result
		clone := []int{}
		clone = append(clone, res[len(res)-1]...)
		clone = clone[1:]
		clone = append(clone, nums[i])
		// append to res
		res = append(res, clone)
	}
	return res
}

func main() {
	fmt.Println(windowSum1([]int{}, 3))
	fmt.Println(windowSum1([]int{1, 2, 3, 4, 5, 6, 7}, -1))
	fmt.Println(windowSum1([]int{1, 2, 3, 4, 5, 6, 7}, 8))
	fmt.Println(windowSum1([]int{1, 2, 3, 4, 5, 6, 7}, 3))

	fmt.Println(windowSum2([]int{}, 3))
	fmt.Println(windowSum2([]int{1, 2, 3, 4, 5, 6, 7}, -1))
	fmt.Println(windowSum2([]int{1, 2, 3, 4, 5, 6, 7}, 8))
	fmt.Println(windowSum2([]int{1, 2, 3, 4, 5, 6, 7}, 3))
}
