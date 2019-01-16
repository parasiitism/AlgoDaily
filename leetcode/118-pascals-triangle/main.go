package main

import "fmt"

/*
	1st approach:
	- intuitive approach inspired by the desc
	Time		O(n!)
	Space		O(n!) the result
	16jan2019
*/
func generate(numRows int) [][]int {
	if numRows == 0 {
		return [][]int{}
	}
	if numRows == 1 {
		return [][]int{
			{1},
		}
	}
	if numRows == 1 {
		return [][]int{
			{1},
			{1, 1},
		}
	}
	res := [][]int{
		{1},
		{1, 1},
	}
	for i := 2; i < numRows; i++ {
		for j := 0; j <= i; j++ {
			if j == 0 {
				res = append(res, []int{1})
			} else if j < i {
				temp := res[i-1][j-1] + res[i-1][j]
				res[i] = append(res[i], temp)
			} else {
				res[i] = append(res[i], 1)
			}
		}
	}
	return res
}

func main() {
	fmt.Println(generate(0))
	fmt.Println(generate(1))
	fmt.Println(generate(2))
	fmt.Println(generate(5))
	fmt.Println(generate(10))
}
