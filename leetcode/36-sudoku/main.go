package main

import "fmt"

// very straight forward solution
// O(3n)
// beats 31.25%
func isValidSudoku(board [][]byte) bool {
	for i := 0; i < 9; i++ {
		hash := make(map[byte]bool)
		for j := 0; j < 9; j++ {
			_, e := hash[board[i][j]]
			if e && board[i][j] != '.' {
				return false
			}
			hash[board[i][j]] = true
		}
	}
	for i := 0; i < 9; i++ {
		hash := make(map[byte]bool)
		for j := 0; j < 9; j++ {
			_, e := hash[board[j][i]]
			if e && board[j][i] != '.' {
				return false
			}
			hash[board[j][i]] = true
		}
	}
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if check3x3(board, i, j) == false {
				return false
			}
		}
	}
	return true
}

func check3x3(board [][]byte, x int, y int) bool {
	hash := make(map[byte]bool)
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			_, e := hash[board[x*3+i][y*3+j]]
			if e && board[x*3+i][y*3+j] != '.' {
				return false
			}
			hash[board[x*3+i][y*3+j]] = true
		}
	}
	return true
}

func main() {
	a := [][]byte{
		{'5', '3', '.', '.', '7', '.', '.', '.', '.'},
		{'6', '.', '.', '1', '9', '5', '.', '.', '.'},
		{'.', '9', '8', '.', '.', '.', '.', '6', '.'},
		{'8', '.', '.', '.', '6', '.', '.', '.', '3'},
		{'4', '.', '.', '8', '.', '3', '.', '.', '1'},
		{'7', '.', '.', '.', '2', '.', '.', '.', '6'},
		{'.', '6', '.', '.', '.', '.', '2', '8', '.'},
		{'.', '.', '.', '4', '1', '9', '.', '.', '5'},
		{'.', '.', '.', '.', '8', '.', '.', '7', '9'},
	}
	fmt.Println(isValidSudoku(a))
}
