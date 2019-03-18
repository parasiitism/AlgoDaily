package main

import "fmt"

/*
	sort a stack using a stack
	https://www.youtube.com/watch?v=nll-b4GeiX4
*/

/*
	idea similar to insertion sort

	Time average O(n^2)
	Time best O(n) if the input stack is reversed, e.g. [4,3,2,1]
	Time worst O(n^2) if the input stack is sorted, e.g. [1,2,3,4]
*/

func sortStack(stack []int) []int {
	helperStack := []int{}
	for len(stack) > 0 {
		// pop main stack
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		// count
		// cnt := 0
		for len(helperStack) > 0 && helperStack[len(helperStack)-1] < pop {
			// pop helper stack
			hp := helperStack[len(helperStack)-1]
			helperStack = helperStack[:len(helperStack)-1]
			// put it into mainstack for now
			stack = append(stack, hp)
			// count +1
			// cnt++
		}
		helperStack = append(helperStack, pop)
		// the below operation is not necessary because we will need to do it in the later iteration
		// for i := 0; i < cnt; i++ {
		// 	// pop main stack until we reach cnt
		// 	p := stack[len(stack)-1]
		// 	stack = stack[:len(stack)-1]
		// 	// pop mainstack
		// 	helperStack = append(helperStack, p)
		// }
	}
	// the reverse order of the helperstack is the result
	return helperStack
}

func main() {
	a := []int{3, 1, 2, 4}
	fmt.Println(sortStack(a))
}
