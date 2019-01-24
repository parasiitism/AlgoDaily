package main

import (
	"fmt"
	"math"
)

/*
	- no zeros?
*/

func productExceptSelf(nums []int) []int {
	product := 1
	hasZero := false
	for _, num := range nums {
		if num == 0 && hasZero == false {
			hasZero = true
		} else {
			product *= num
		}
	}
	res := []int{}
	for _, num := range nums {
		if num == 0 {
			res = append(res, product)
		} else {
			if hasZero {
				res = append(res, 0)
			} else {
				res = append(res, product/num)
			}
		}
	}
	return res
}

/*
	follow up: do it without using division
	- TLE
	it takes too long to use naive division using subtraction
*/
func productExceptSelf1(nums []int) []int {
	product := 1
	hasZero := false
	for _, num := range nums {
		if num == 0 && hasZero == false {
			hasZero = true
		} else {
			product *= num
		}
	}
	res := []int{}
	for _, num := range nums {
		if num == 0 {
			res = append(res, product)
		} else {
			if hasZero {
				res = append(res, 0)
			} else {
				res = append(res, divideWithoutDivision(product, num))
			}
		}
	}
	return res
}

// 6 = 3*2 = 2+2+2
func divideWithoutDivision(dividend int, divisor int) int {
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
	fmt.Println(productExceptSelf([]int{1, 2, 3, 4}))
	fmt.Println(productExceptSelf([]int{1, 2, 3, 4, 0}))
	fmt.Println(productExceptSelf([]int{1, 2, 3, 4, 0, 0}))
	// follow up
	fmt.Println(divideWithoutDivision(6, 2))
	fmt.Println(divideWithoutDivision(6, -2))
	fmt.Println(divideWithoutDivision(-6, 2))
	fmt.Println(divideWithoutDivision(-6, -2))

	fmt.Println(productExceptSelf1([]int{1, 2, 3, 4}))
	fmt.Println(productExceptSelf1([]int{1, 2, 3, 4, 0}))
	fmt.Println(productExceptSelf1([]int{1, 2, 3, 4, 0, 0}))

	fmt.Println(productExceptSelf1([]int{1, -1}))
}
