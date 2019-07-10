package main

import "fmt"

/*
This is a demo task.

Write a function:

func Solution(A []int) int

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
*/

func Solution(A []int) int {
	// write your code in Go 1.4
	seen := make([]bool, len(A)+1)
	for i := 0; i < len(A); i++ {
		if A[i]-1 >= 0 {
			seen[A[i]-1] = true
		}
	}
	fmt.Println(seen)
	for i := 0; i < len(seen); i++ {
		if seen[i] == false {
			return i + 1
		}
	}
	return -1
}

func main() {
	fmt.Println(Solution([]int{1, 3, 6, 4, 1, 2}))
	fmt.Println(Solution([]int{1, 2, 3}))
}
