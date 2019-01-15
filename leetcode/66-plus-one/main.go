package main

import "fmt"

/*
	naive approach:
	- convert to an integer
	- add 1
	- convert back to digits
	Problematic for a very large input array
*/
func plusOne1(digits []int) []int {
	num := 0
	for i := 0; i < len(digits); i++ {
		num = num*10 + digits[i]
	}
	num += 1
	arr := []int{}
	for num > 0 {
		mod := num % 10
		arr = append([]int{mod}, arr...)
		num /= 10
	}
	return arr
}

/*
	better approach:
	- reversely, add 1 on each digit until the digit !=9
	Time	O(n)
	Space O(1)
	15jan2019
*/
func plusOne(digits []int) []int {
	last := len(digits) - 1
	if digits[last] != 9 {
		digits[last] += 1
		return digits
	}
	i := len(digits) - 1
	shouldGoOn := true
	for i >= 0 && shouldGoOn {
		temp := digits[i] + 1
		if temp > 9 {
			digits[i] = 0
			if i == 0 {
				digits = append([]int{1}, digits...)
			}
		} else {
			digits[i] = temp
			shouldGoOn = false
		}
		i--
	}
	return digits
}

func main() {
	fmt.Println(plusOne([]int{4, 3, 2, 1}))
	fmt.Println(plusOne([]int{9, 9}))
	fmt.Println(plusOne([]int{1, 0, 9, 9}))
	fmt.Println(plusOne([]int{7, 2, 8, 5, 0, 9, 1, 2, 9, 5, 3, 6, 6, 7, 3, 2, 8, 4, 3, 7, 9, 5, 7, 7, 4, 7, 4, 9, 4, 7, 0, 1, 1, 1, 7, 4, 0, 0, 6}))
}
