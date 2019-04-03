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

func main() {

}
