package main

import (
	"fmt"
)

func exist(board [][]byte, word string) bool {
	if len(word) == 0 {
		return false
	}
	// find the "heads" in the matrix
	head := word[0]
	byte_word := []byte(word)
	for row := 0; row < len(board); row++ {
		for col := 0; col < len(board[0]); col++ {
			if board[row][col] == head {
				if dfs(row, col, byte_word, board) {
					return true
				}
			}
		}
	}
	return false
}

func dfs(row int, col int, tail []byte, board [][]byte) bool {
	if row < 0 || row >= len(board) {
		return false
	}
	if col < 0 || col >= len(board[row]) {
		return false
	}
	if board[row][col] != tail[0] {
		return false
	}
	// board[row][col] == tail[0] now
	if len(tail) == 1 {
		return true
	}

	temp := board[row][col]
	board[row][col] = '.'

	t := tail[1:]
	found := dfs(row-1, col, t, board) ||
		dfs(row+1, col, t, board) ||
		dfs(row, col-1, t, board) ||
		dfs(row, col+1, t, board)

	board[row][col] = temp

	return found
}

func main() {
	// false
	matrix := [][]byte{
		{'A', 'B', 'C', 'E'},
		{'S', 'F', 'C', 'S'},
		{'A', 'D', 'E', 'E'},
	}
	fmt.Println(exist(matrix, "ABCCEDG"))

	// true
	matrix = [][]byte{
		{'a', 'b'},
		{'c', 'd'},
	}
	fmt.Println(exist(matrix, "cdba"))

	// true
	matrix = [][]byte{
		{'A', 'B', 'C', 'E'},
		{'S', 'F', 'E', 'S'},
		{'A', 'D', 'E', 'E'},
	}
	fmt.Println(exist(matrix, "ABCESEEEFS"))

	// false
	matrix = [][]byte{
		{'a', 'a'},
	}
	fmt.Println(exist(matrix, "aaa"))
}
