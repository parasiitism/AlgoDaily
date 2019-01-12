package main

import "fmt"

type NumMatrix struct {
	Matrix [][]int
}

func Constructor(matrix [][]int) NumMatrix {
	return NumMatrix{matrix}
}

func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	result := 0
	for i := row1; i <= row2; i++ {
		for j := col1; j <= col2; j++ {
			result += this.Matrix[i][j]
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
