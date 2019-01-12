package main

import "fmt"

/*
	1st attempt
	- similar approach to the leetcode 303
	Time of Constructor O(n)
	Space of Constructor O(n)
	Time of SumRange O(n)
	Space of SumRange O(1)
	52ms beats 80%
*/
type NumMatrix struct {
	Arr [][]int
}

func Constructor(matrix [][]int) NumMatrix {
	arr := [][]int{}
	for i := 0; i < len(matrix); i++ {
		temp := []int{}
		sum := 0
		for j := 0; j < len(matrix[i]); j++ {
			sum += matrix[i][j]
			temp = append(temp, sum)
		}
		arr = append(arr, temp)
	}
	return NumMatrix{arr}
}

func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	result := 0
	for i := row1; i <= row2; i++ {
		if col1 == 0 {
			result += this.Arr[i][col2]
		} else if col1 <= col2 {
			result += this.Arr[i][col2] - this.Arr[i][col1-1]
		}
	}
	return result
}

func main() {
	m := [][]int{
		[]int{3, 0, 1, 4, 2},
		[]int{5, 6, 3, 2, 1},
		[]int{1, 2, 0, 1, 5},
		[]int{4, 1, 0, 1, 7},
		[]int{1, 0, 3, 0, 5},
	}
	c := Constructor(m)
	fmt.Println(c.SumRegion(2, 1, 4, 3))
	fmt.Println(c.SumRegion(1, 1, 2, 2))
	fmt.Println(c.SumRegion(1, 2, 2, 4))
}
