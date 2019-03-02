package main

import "fmt"

/*
	1st approach
	1. copy the board
	2. iterate through the clone and change the cells' state in the original board
	3. check neighers' state
	4. mutate the cell's value

	Time	O(m*n)
	Space	O(m*n) the copy
	0 ms, faster than 100.00%
*/
func gameOfLife(board [][]int) {
	// copy the board
	clone := [][]int{}
	for i := 0; i < len(board); i++ {
		temp := []int{}
		for j := 0; j < len(board[0]); j++ {
			temp = append(temp, board[i][j])
		}
		clone = append(clone, temp)
	}
	// iterate through the clone and change the cells' state in the original board
	for i := 0; i < len(clone); i++ {
		for j := 0; j < len(clone[0]); j++ {
			// check neighers' state
			count := 0
			if i-1 >= 0 && j-1 >= 0 && clone[i-1][j-1] == 1 {
				count++
			}
			if i-1 >= 0 && clone[i-1][j] == 1 {
				count++
			}
			if i-1 >= 0 && j+1 < len(clone[0]) && clone[i-1][j+1] == 1 {
				count++
			}
			if j+1 < len(clone[0]) && clone[i][j+1] == 1 {
				count++
			}
			if i+1 < len(clone) && j+1 < len(clone[0]) && clone[i+1][j+1] == 1 {
				count++
			}
			if i+1 < len(clone) && clone[i+1][j] == 1 {
				count++
			}
			if i+1 < len(clone) && j-1 >= 0 && clone[i+1][j-1] == 1 {
				count++
			}
			if j-1 >= 0 && clone[i][j-1] == 1 {
				count++
			}
			// mutate the cell's value
			if clone[i][j] == 1 {
				if count > 1 && count < 4 {
					board[i][j] = 1
				} else {
					board[i][j] = 0
				}
			}
			if clone[i][j] == 0 {
				if count == 3 {
					board[i][j] = 1
				} else {
					board[i][j] = 0
				}
			}
		}
	}
}

func main() {
	a := [][]int{
		{0, 1, 0},
		{0, 0, 1},
		{1, 1, 1},
		{0, 0, 0},
	}
	gameOfLife(a)
	fmt.Println(a)
}
