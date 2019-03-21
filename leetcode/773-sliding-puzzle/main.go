package main

import (
	"fmt"
	"strconv"
)

/*
	1st approach: bfs + hashset to avoid redundant traversal

	Time    O(n!) the total number of permutation of the board states
	Space   O(n!)
	12 ms, faster than 48.57%
*/

type QItem struct {
	Board [][]int
	Steps int
}

func slidingPuzzle(board [][]int) int {
	// to avoid vistied states
	seen := make(map[string]bool)
	// bfs
	q := []QItem{}
	q = append(q, QItem{board, 0})
	for len(q) > 0 {
		head := q[0]
		q = q[1:]
		b, steps := head.Board, head.Steps

		// check if the the state is visited
		key := stringifyBoard(b)
		if _, x := seen[key]; x {
			continue
		}
		seen[key] = true

		// enqueue the variations if final state not reach
		if key == "123450" {
			return steps
		}
		for i := 0; i < len(board); i++ {
			for j := 0; j < len(board[i]); j++ {
				if b[i][j] == 0 {
					if i-1 >= 0 {
						temp := cloneBoard(b)
						temp[i-1][j], temp[i][j] = temp[i][j], temp[i-1][j]
						q = append(q, QItem{temp, steps + 1})
					}
					if i+1 < len(board) {
						temp := cloneBoard(b)
						temp[i+1][j], temp[i][j] = temp[i][j], temp[i+1][j]
						q = append(q, QItem{temp, steps + 1})
					}
					if j-1 >= 0 {
						temp := cloneBoard(b)
						temp[i][j-1], temp[i][j] = temp[i][j], temp[i][j-1]
						q = append(q, QItem{temp, steps + 1})
					}
					if j+1 < len(board[0]) {
						temp := cloneBoard(b)
						temp[i][j+1], temp[i][j] = temp[i][j], temp[i][j+1]
						q = append(q, QItem{temp, steps + 1})
					}
				}
			}
		}
	}
	return -1
}

func stringifyBoard(board [][]int) string {
	s := ""
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[i]); j++ {
			s += strconv.Itoa(board[i][j])
		}
	}
	return s
}

func cloneBoard(board [][]int) [][]int {
	temp := [][]int{}
	for i := 0; i < len(board); i++ {
		arr := []int{}
		for j := 0; j < len(board[i]); j++ {
			arr = append(arr, board[i][j])
		}
		temp = append(temp, arr)
	}
	return temp
}

func main() {
	a := [][]int{
		{1, 2, 3},
		{4, 0, 5},
	}
	fmt.Println(slidingPuzzle(a))
	a = [][]int{
		{1, 2, 3},
		{5, 4, 0},
	}
	fmt.Println(slidingPuzzle(a))
	a = [][]int{
		{4, 1, 2},
		{5, 0, 3},
	}
	fmt.Println(slidingPuzzle(a))
	a = [][]int{
		{3, 2, 4},
		{1, 5, 0},
	}
	fmt.Println(slidingPuzzle(a))
}
