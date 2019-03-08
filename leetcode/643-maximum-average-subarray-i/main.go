package main

import (
	"fmt"
	"math"
)

func findMaxAverage(nums []int) float64 {
	if len(nums) == 0 {
		return 0
	}
	dp := [][]int{}
	firstItem := []int{nums[0], 1} // [sum, count] count can be either heritate from the previuous item(+1) or the item itself(1)
	dp = append(dp, firstItem)
	for i := 1; i < len(nums); i++ {
		temp := []int{}
		if dp[i-1][0]+nums[i] > nums[i] {
			temp = []int{dp[i-1][0] + nums[i], dp[i-1][1] + 1}
		} else {
			temp = []int{nums[i], 1}
		}
		dp = append(dp, temp)
	}
	res := -math.MaxFloat64
	for i := 0; i < len(dp); i++ {
		if float64(dp[i][0]) > res {
			res = float64(dp[i][0]) / float64(dp[i][1])
		}
	}
	return res
}

func main() {
	fmt.Println(findMaxAverage([]int{1, 12, -5, -6, 50, 3}))
}
