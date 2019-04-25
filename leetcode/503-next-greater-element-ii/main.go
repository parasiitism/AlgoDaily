package main

import (
	"fmt"
	"strconv"
)

/*
	it is a follow up question when the array is not circular
	https://www.youtube.com/watch?v=uFso48YRRao

	questions to ask:
	- will there be duplicate numbers? yes
*/

/*
	brute force: O(n^2)
*/

/*
	modified classic approach: stack + hashtable
	- classic approach: https://www.youtube.com/watch?v=uFso48YRRao
	- save the index of a number as well such that we can know which number it refers to

	Time		O(2n)
	Space		O(n)
	400 ms, faster than 57.14%
*/
func nextGreaterElements(nums []int) []int {
	// b = a + a
	circular := []int{}
	circular = append(circular, nums...)
	circular = append(circular, nums...)
	// since there might be duplicate we save the index as well
	// see if the current element is the target of peek elements in the stack
	stack := [][]int{} // (num, idx)
	m := make(map[string]int)
	for i := 0; i < len(circular); i++ {
		num := circular[i]
		for len(stack) > 0 && num > stack[len(stack)-1][0] {
			key := strconv.Itoa(stack[len(stack)-1][0]) + "at" + strconv.Itoa(stack[len(stack)-1][1])
			m[key] = num
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, []int{num, i})
	}
	// construct the result
	res := []int{}
	for i := 0; i < len(nums); i++ {
		num := nums[i]
		key := strconv.Itoa(num) + "at" + strconv.Itoa(i)
		if v, x := m[key]; x {
			res = append(res, v)
		} else {
			res = append(res, -1)
		}
	}
	return res
}

func main() {
	fmt.Println(nextGreaterElements([]int{1, 2, 1}))
	fmt.Println(nextGreaterElements([]int{2, 3, 5, 1, 0, 7, 3, 6}))
	fmt.Println(nextGreaterElements([]int{5, 3, 2, 10, 6, 8, 1, 4, 12, 7, 4}))
}
