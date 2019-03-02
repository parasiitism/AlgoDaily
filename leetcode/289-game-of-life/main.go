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

/*
	2nd approach: bit operation
	- since the 1st approach use an extra array to store the state but the state only stores 0 and 1, 1 bit
	we can actually use the 2nd bit to store the next state
	e.g. [2nd bit, 1st bit] = [next state, current state]
	- To get the current state, simply do board[i][j] & 1
	- To get the next state, simply do board[i][j] >> 1

	Time	O(m*n)
	Space	O(1) we use the bits in the original cells
	0 ms, faster than 100.00%
*/
func gameOfLife1(board [][]int) {
	// iterate through the clone and change the cells' state in the original board
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			// check neighers' state
			count := 0
			if i-1 >= 0 && j-1 >= 0 && board[i-1][j-1]&1 == 1 {
				count++
			}
			if i-1 >= 0 && board[i-1][j]&1 == 1 {
				count++
			}
			if i-1 >= 0 && j+1 < len(board[0]) && board[i-1][j+1]&1 == 1 {
				count++
			}
			if j+1 < len(board[0]) && board[i][j+1]&1 == 1 {
				count++
			}
			if i+1 < len(board) && j+1 < len(board[0]) && board[i+1][j+1]&1 == 1 {
				count++
			}
			if i+1 < len(board) && board[i+1][j]&1 == 1 {
				count++
			}
			if i+1 < len(board) && j-1 >= 0 && board[i+1][j-1]&1 == 1 {
				count++
			}
			if j-1 >= 0 && board[i][j-1]&1 == 1 {
				count++
			}
			// mutate the cell's value
			if board[i][j]&1 == 1 {
				if count > 1 && count < 4 {
					board[i][j] += 2 // 01 -> 11
				}
			}
			if board[i][j]&1 == 0 {
				if count == 3 {
					board[i][j] += 2 // 00 -> 10
				}
			}
		}
	}
	// get the next state
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			board[i][j] >>= 1
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
