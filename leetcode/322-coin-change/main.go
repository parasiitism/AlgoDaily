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
// beats 13.75%
func coinChange(coins []int, amount int) int {
	var q []Queue
	hash := make(map[int]bool)
	hash[amount] = true
	q = append(q, Queue{amount, 0})
	min := math.MaxUint32
	for len(q) > 0 {
		n := len(q)
		for i := 0; i < n; i++ {
			head := q[0]
			q = q[1:]
			if head.amount == 0 {
				// since we are doing bfs, from top to bottom,
				// once we reach to 0, it means this is the shortest path
				return head.steps
			}
			for j := 0; j < len(coins); j++ {
				coin := coins[j]
				next := head.amount - coin
				_, x := hash[next]
				if next >= 0 && !x {
					q = append(q, Queue{next, head.steps + 1})
					hash[next] = true
				}
			}
		}
	}
	if min == math.MaxUint32 {
		return -1
	}
	return min
}

// 2nd attempt
// dfs + hashtable
// count steps from bottom to top; memorize the min steps for calculated amount
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

func main() {
	fmt.Println(coinChange([]int{5}, 5))
	fmt.Println(coinChange([]int{1, 2, 5}, 7))
	fmt.Println(coinChange([]int{2}, 3))
	fmt.Println(coinChange([]int{1, 7, 11, 13, 17}, 152))

	fmt.Println(coinChange1([]int{5}, 5))
	fmt.Println(coinChange1([]int{1, 2, 5}, 7))
	fmt.Println(coinChange1([]int{2}, 3))
	fmt.Println(coinChange1([]int{1, 7, 11, 13, 17}, 152))
}
