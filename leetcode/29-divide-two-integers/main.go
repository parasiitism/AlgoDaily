package main

import "math"

/*
	1st approach
	- 6 = 3*2 = 2+2+2, 7 = 3*2 = 2+2+2+1
	- be careful of the negative
	- be careful of the boundaries
	Time		O(quotient)
	Space		O(1)
	2980ms beats 23.65%
	24jan2019
*/
func divide(dividend int, divisor int) int {
	sign := 1
	if (dividend < 0 && divisor > 0) || (dividend > 0 && divisor < 0) {
		sign = -1
	}
	if dividend < 0 {
		dividend = -dividend
	}
	if divisor < 0 {
		divisor = -divisor
	}
	cnt := 0
	for dividend >= divisor {
		dividend -= divisor
		cnt++
	}
	temp := sign * cnt
	if temp < math.MinInt32 {
		return math.MinInt32
	}
	if temp > math.MaxInt32 {
		return math.MaxInt32
	}
	return temp
}

func main() {

}
