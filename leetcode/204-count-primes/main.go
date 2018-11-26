package main

import "fmt"

func countPrimes(n int) int {
	if n < 3 {
		return 0
	} else if n == 3 {
		return 1
	}
	result := 0
	for i := 2; i < n; i++ {
		// check if prime
		isPrime := true
		for j := 2; j < i; j++ {
			if i%j == 0 {
				isPrime = false
				break
			}
		}
		if isPrime {
			result++
		}
	}
	return result
}

func main() {
	// 499979

	fmt.Println(countPrimes(10))
}
