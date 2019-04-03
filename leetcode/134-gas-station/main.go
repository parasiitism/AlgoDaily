package main

/*
	1st approach: brute force

	Time    O(n^2)
	Space   O(n)
	24 ms, faster than 35.29%
*/
func canCompleteCircuit(gas []int, cost []int) int {
	n := len(gas)
	gas = append(gas, gas...)
	cost = append(cost, cost...)
	for i := 0; i < n; i++ {
		acc := 0
		success := true
		for j := i; j < i+n; j++ {
			acc += gas[j] - cost[j]
			if acc < 0 {
				success = false
				break
			}
		}
		if success {
			return i
		}
	}
	return -1
}

/*
	2nd approach: greedy
	1. total gas must >= total cost
	2. if gas[i]-cost[i], means we can move forward
	3. we can save the cost from the left, if costFromLeft >= 0, it means we can make it

	e.g.1
	gas  = [1, 2, 3, 4, 5]
	cost = [3, 4, 5, 1, 2]
	left = [-2,-4,-6,-3,0]
	from index 3, gas[i]-cost[i] has been > 0

	e.g.2
	gas  = [1, 2, 3, 4, 5, 1]
	cost = [3, 4, 5, 1, 2, 8]
	left = [-2,-4,-6,-3,0, -7]
	left < 0, not possbile

	e.g.3
	gas  = [1, 2, 3, 4, 5, 1, 8]
	cost = [3, 4, 5, 1, 2, 8, 1]
	left = [-2,-4,-6,-3,0, -7, 0]
	from index 6, gas[i]-cost[i] has been > 0

	e.g.4
	gas  = [2, 3, 4]
	cost = [3, 4, 3]
	left = [-1,-2,-1]
	left < 0, not possbile

	ref:
	- https://leetcode.com/articles/gas-station/

	Time    O(n)
	Space   O(n)
	4 ms, faster than 100.00%
*/
func canCompleteCircuit1(gas []int, cost []int) int {
	costFromLeft := 0
	curCost := 0
	start := 0
	for i := 0; i < len(gas); i++ {
		costFromLeft += gas[i] - cost[i]
		curCost += gas[i] - cost[i]
		if curCost < 0 {
			start = i + 1
			curCost = 0
		}
	}
	if costFromLeft < 0 {
		return -1
	}
	return start
}

func main() {

}
