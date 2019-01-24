package main

import "fmt"

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
	follow up:
	- do it without using division
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
func divideWithoutDivision(num int, target int) int {
	sign := 1
	if (num < 0 && target > 0) || (num > 0 && target < 0) {
		sign = -1
	}

	if num < 0 {
		num = -num
	}

	if target < 0 {
		target = -target
	}

	cnt := 0
	for num >= target {
		num -= target
		cnt++
	}
	return sign * cnt
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
