package main

import "fmt"

/*
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
*/

// the data set is small, brute-force approach should be good enough
func computeAmicableSum(n int) int {
	hash := make(map[int]int)
	result := 0
	for i := 1; i <= n; i++ {
		temp := computeDivisorSum(i)
		if hash[temp] == i {
			result += temp + i
		}
		hash[i] = temp
	}
	return result
}

func computeDivisorSum(n int) int {
	divs := []int{}
	for i := 1; i < n; i++ {
		if n%i == 0 {
			divs = append(divs, i)
		}
	}
	sum := 0
	for i := 0; i < len(divs); i++ {
		sum += divs[i]
	}
	return sum
}

func main() {
	fmt.Println(computeAmicableSum(10000))
}
