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

func main() {
	fmt.Println(coinChange([]int{5}, 5))
	fmt.Println(coinChange([]int{1, 2, 5}, 7))
	fmt.Println(coinChange([]int{2}, 3))
	fmt.Println(coinChange([]int{1, 7, 11, 13, 17}, 152))
}
