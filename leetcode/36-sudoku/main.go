package main

import (
	"fmt"
	"strconv"
)

/*
	1st: very straight forward solution
	time		O(3n)
	space 	O(n)
	beats 31.25%
*/
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

/*
	2nd attempt
	use 3 hashtables
	"5" in row 1 => 1,5
	"5" in row 1 => 1,5
	"5" in box 1 => 1,5

	time 	O(n)
	space 	O(n)
	beats 31.25%
*/
func isValidSudoku1(board [][]byte) bool {
	rowHash := make(map[string]bool)
	colHash := make(map[string]bool)
	boxHash := make(map[string]bool)
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			if board[i][j] == '.' {
				continue
			}
			temp := string(board[i][j])
			rowKey := strconv.Itoa(i) + "," + temp
			if _, x := rowHash[rowKey]; x {
				return false
			}
			rowHash[rowKey] = true

			colKey := strconv.Itoa(j) + "," + temp
			if _, x := colHash[colKey]; x {
				return false
			}
			colHash[colKey] = true

			boxKey := strconv.Itoa(i/3*3+j/3) + "," + temp
			if _, x := boxHash[boxKey]; x {
				return false
			}
			boxHash[boxKey] = true
		}
	}
	return true
}

/*
	2nd attempt
	the 2nd attempt can be optimied as using 1 hashtable
	"5" in row 1 => 1row5
	"5" in row 1 => 1col5
	"5" in box 1 => 1box5
	time 	O(n)
	space 	O(n)
	beats 31.25%
*/
func isValidSudoku2(board [][]byte) bool {
	hash := make(map[string]bool)
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			if board[i][j] == '.' {
				continue
			}
			temp := string(board[i][j])

			rowKey := strconv.Itoa(i) + "row" + temp
			if _, x := hash[rowKey]; x {
				return false
			}
			hash[rowKey] = true

			colKey := strconv.Itoa(j) + "col" + temp
			if _, x := hash[colKey]; x {
				return false
			}
			hash[colKey] = true

			boxKey := strconv.Itoa(i/3*3+j/3) + "box" + temp
			if _, x := hash[boxKey]; x {
				return false
			}
			hash[boxKey] = true
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
	fmt.Println(isValidSudoku2(a))
}
