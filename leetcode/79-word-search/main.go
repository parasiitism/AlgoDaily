package main

import (
	"fmt"
	"strconv"
)

func exist(board [][]byte, word string) bool {
	// find the "heads" in the matrix
	head := word[0]
	candidates := [][]int{}
	for row := 0; row < len(board); row++ {
		for col := 0; col < len(board[0]); col++ {
			if board[row][col] == head {
				candidates = append(candidates, []int{row, col})
			}
		}
	}
	// for each head, find the path

	// declare rescursion
	var dfs func(row int, col int, tail string, history map[string]bool) bool
	dfs = func(row int, col int, tail string, history map[string]bool) bool {
		if row < 0 || row+1 > len(board) || col < 0 || col+1 > len(board[0]) || len(tail) < 1 {
			return false
		}

		i := strconv.Itoa(row)
		j := strconv.Itoa(col)
		key := i + "," + j

		if _, existed := history[key]; existed {
			return false
		}
		if board[row][col] == tail[0] {

			new_history := make(map[string]bool)
			for k, v := range history {
				new_history[k] = v
			}
			new_history[key] = true

			if len(tail) == 1 {
				return true
			} else if len(tail) > 1 {
				t := tail[1:]
				a := dfs(row-1, col, t, new_history)
				b := dfs(row+1, col, t, new_history)
				c := dfs(row, col-1, t, new_history)
				d := dfs(row, col+1, t, new_history)
				return a || b || c || d
			}
		}
		return false
	}

	for i := 0; i < len(candidates); i++ {
		candidate := candidates[i]
		if dfs(candidate[0], candidate[1], word, make(map[string]bool)) {
			return true
		}
	}

	return false
}

func main() {
	matrix := [][]byte{
		{'A', 'B', 'C', 'E'},
		{'S', 'F', 'C', 'S'},
		{'A', 'D', 'E', 'E'},
	}
	fmt.Println(exist(matrix, "ABCCEDG"))

	matrix = [][]byte{
		{'a', 'b'},
		{'c', 'd'},
	}
	fmt.Println(exist(matrix, "cdba"))

	matrix = [][]byte{
		{'A', 'B', 'C', 'E'},
		{'S', 'F', 'E', 'S'},
		{'A', 'D', 'E', 'E'},
	}
	fmt.Println(exist(matrix, "ABCESEEEFS"))

	matrix = [][]byte{
		{'a', 'a'},
	}
	fmt.Println(exist(matrix, "aaa"))
}
