package main

import "fmt"

/*
	2nd approach: optimize the 1st approach
	- try to compensate some space for optimization
	- save the maxprofit on each day when we traverse forward
	- save the maxprofit on each day when we traverse backward
	- the result will be the max sum of profit on day i, which is forward[i]+backward[i]

	Time    O(2n)
	Space   O(1)
	140 ms, faster than 33.82%
*/

func maxProfit(prices []int) int {
	if len(prices) < 2 {
		return 0
	}
	n := len(prices)
	// save the maxprofit on each day when we traverse forward
	bay := prices[0]
	forwardDiff := 0
	forwardDiffs := []int{}
	for i := 0; i < n; i++ {
		price := prices[i]
		if price < bay {
			bay = price
		}
		if price-bay > forwardDiff {
			forwardDiff = price - bay
		}
		forwardDiffs = append(forwardDiffs, forwardDiff)
	}
	// save the maxprofit on each day when we traverse backward
	peak := prices[n-1]
	backwardDiff := 0
	backwardDiffs := []int{}
	for i := n - 1; i >= 0; i-- {
		price := prices[i]
		if price > peak {
			peak = price
		}
		if peak-price > backwardDiff {
			backwardDiff = peak - price
		}
		backwardDiffs = append([]int{backwardDiff}, backwardDiffs...)
	}
	// the result will be the max sum of profit on day i, which is forward[i]+backward[i]
	result := 0
	for i := 0; i < n; i++ {
		temp := forwardDiffs[i] + backwardDiffs[i]
		if temp > result {
			result = temp
		}
	}
	return result
}

func main() {
	fmt.Println(maxProfit([]int{3, 3, 5, 0, 0, 3, 1, 4}))
	fmt.Println(maxProfit([]int{1, 2, 3, 4, 5}))
	fmt.Println(maxProfit([]int{7, 6, 4, 3, 1}))
	fmt.Println(maxProfit([]int{7, 1, 5, 3, 6, 4}))
}
