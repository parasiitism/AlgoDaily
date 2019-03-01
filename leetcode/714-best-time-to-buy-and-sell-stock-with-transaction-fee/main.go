package main

import "fmt"

func maxProfit(prices []int, fee int) int {
	if len(prices) < 2 {
		return 0
	}
	last := prices[0]
	bay := prices[0]
	res := 0
	for i, price := range prices {
		if price >= last {
			last = price
			if i+1 == len(prices) && last-bay > fee {
				res += last - bay - fee
			}
		} else {
			if last-bay > fee {
				res += last - bay - fee
				bay = price
				last = price
			}
		}
	}
	return res
}

func main() {
	fmt.Println(maxProfit([]int{1, 3, 2, 8, 4, 9}, 2))
}
