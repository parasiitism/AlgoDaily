package main

import (
	"fmt"
	"math"
)

type Queue struct {
	amount int
	steps  int
}

// 1st attempt:
// bfs(from top to bottom) + hashtable(avoid redundant calculation)
// 188 ms, faster than 15.89%
func coinChange(coins []int, amount int) int {
	var q []Queue
	hash := make(map[int]bool)
	q = append(q, Queue{amount, 0})
	for len(q) > 0 {
		n := len(q)
		for i := 0; i < n; i++ {
			head := q[0]
			q = q[1:]

			if _, x := hash[head.amount]; x {
				continue
			}
			hash[head.amount] = true

			if head.amount == 0 {
				// since we are doing bfs, from top to bottom,
				// once we reach to 0, it means this is the shortest path
				return head.steps
			} else if head.amount > 0 {
				for j := 0; j < len(coins); j++ {
					coin := coins[j]
					next := head.amount - coin
					q = append(q, Queue{next, head.steps + 1})
				}
			}
		}
	}
	return -1
}

// 2nd attempt
// dfs + hashtable
// count steps from top to bottom; memorize the min steps for calculated amount
// beats 25.32%
func coinChange1(coins []int, amount int) int {
	hash := make(map[int]int)
	result := dfs(coins, amount, hash)
	if result == math.MaxUint32 {
		return -1
	}
	return result
}

func dfs(coins []int, amount int, hash map[int]int) int {
	if amount == 0 {
		return 0
	} else if amount < 0 {
		return math.MaxUint32
	}
	if v, x := hash[amount]; x {
		return v
	}
	min := math.MaxUint32
	for i := 0; i < len(coins); i++ {
		coin := coins[i]
		temp := dfs(coins, amount-coin, hash)
		if temp+1 < min {
			min = temp + 1
		}
	}
	hash[amount] = min
	return min
}

// 3rd attempt
// learned from others: bottom-up
// e.g. coins = [1,2,5], amount = 7
// f(0) = 0 // so if f(100-100), it output 0+1=1
// f(1) = min(f(1)) + 1
// f(2) = min(f(1)+f(0)) + 1
// f(3) = min(f(2)+f(1)) + 1
// f(4) = min(f(3)+f(2)) + 1
// f(5) = min(f(4)+f(3)+f(0)) + 1
// f(6) = min(f(5)+f(4)+f(1)) + 1
// f(7) = min(f(6)+f(5)+f(2)) + 1
// ...
// this beats 96.2%
func coinChange2(coins []int, amount int) int {
	dp := make([]int, amount+1) // store the min-steps from bottpm to top
	// initialize them by setting each of them a big value
	// except for base case, f(0), because we need f(0) = 0 to calculate the combined steps
	for i := 1; i < len(dp); i++ {
		dp[i] = amount + 1
	}
	// store the steps from bottom to top
	for target := 1; target <= amount; target++ {
		for j := 0; j < len(coins); j++ {
			coin := coins[j]
			if target >= coin && dp[target-coin]+1 < dp[target] {
				dp[target] = dp[target-coin] + 1
			}
		}
	}
	if dp[amount] > amount {
		return -1
	}
	return dp[amount]
}

func main() {
	fmt.Println(coinChange([]int{5}, 5))
	fmt.Println(coinChange([]int{1, 2, 5}, 11))
	fmt.Println(coinChange([]int{2}, 3))
	fmt.Println(coinChange([]int{1, 7, 11, 13, 17}, 152))
	fmt.Println(coinChange([]int{70, 177, 394, 428, 427, 437, 176, 145, 83, 370}, 7582))
	fmt.Println("-----")

	fmt.Println(coinChange1([]int{5}, 5))
	fmt.Println(coinChange1([]int{1, 2, 5}, 11))
	fmt.Println(coinChange1([]int{2}, 3))
	fmt.Println(coinChange1([]int{1, 7, 11, 13, 17}, 152))
	fmt.Println(coinChange([]int{70, 177, 394, 428, 427, 437, 176, 145, 83, 370}, 7582))
	fmt.Println("-----")

	fmt.Println(coinChange2([]int{5}, 5))
	fmt.Println(coinChange2([]int{1, 2, 5}, 11))
	fmt.Println(coinChange2([]int{2}, 3))
	fmt.Println(coinChange2([]int{1, 7, 11, 13, 17}, 152))
	fmt.Println(coinChange([]int{70, 177, 394, 428, 427, 437, 176, 145, 83, 370}, 7582))
}
