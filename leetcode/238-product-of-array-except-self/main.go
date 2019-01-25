package main

import (
	"fmt"
	"math"
)

/*
	Questions to ask:
	- will there be zero?
*/

/*
	naive approach: brute force
	Time		O(n^2)
*/

/*
	naive approach 2: use divide
	but it violates the requirement
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

/*
	3rd approach: learned from others
	- calculate the products from the front & from the back
		e.g.
								2			3 		4 		5
						->	1		1*2		2*3		2*3*4
							3*4*5	4*5		5*1			1		<-
							-----------------------
			result = 60		20		30			12
	- the cruz of the question is to learn this approach, it is slow but it doesn't matter
	Time	O(3n)
	Space	O(2n)
	2836ms beats 5.92%
	25jan2019
*/
func productExceptSelf2(nums []int) []int {
	fromTheFront := []int{1}
	fromTheBack := []int{1}

	n := len(nums)
	for i := 1; i < n; i++ {
		fromTheFront = append(fromTheFront, fromTheFront[i-1]*nums[i-1])
		fromTheBack = append([]int{fromTheBack[0] * nums[n-i]}, fromTheBack...)
	}

	res := []int{}
	for i := 0; i < len(nums); i++ {
		res = append(res, fromTheFront[i]*fromTheBack[i])
	}

	return res
}

func main() {
	fmt.Println(productExceptSelf([]int{1, 2, 3, 4}))
	fmt.Println(productExceptSelf([]int{1, 2, 3, 4, 0}))
	fmt.Println(productExceptSelf([]int{1, 2, 3, 4, 0, 0}))
	fmt.Println(productExceptSelf([]int{1, -1}))

	fmt.Println(productExceptSelf2([]int{1, 2, 3, 4}))
	fmt.Println(productExceptSelf2([]int{1, 2, 3, 4, 0}))
	fmt.Println(productExceptSelf2([]int{1, 2, 3, 4, 0, 0}))
	fmt.Println(productExceptSelf2([]int{1, -1}))
}
