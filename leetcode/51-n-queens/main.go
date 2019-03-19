package main

import "fmt"

/*
	 1st approach: backtracking
	 - https://www.youtube.com/watch?v=5v6zdfkImms
	 - basically try every possisbilities within the safe region
	 - for each coordinate, we need to check the whole board to see if it is safe to place a queen

   Time    O(n^4) for each coordinate, we need to check if safe
   Space   O(n^2)
   12 ms, faster than 57.89%
*/
func solveNQueens(n int) [][]string {
	// init board
	board := BoardConstructor(n)
	// result
	result := [][]string{}

	var backtracking func(b *Board, col, n int)
	backtracking = func(b *Board, col, n int) {
		if col == n {
			// if the col reaches to n, it means we've just found a result
			result = append(result, b.Clone())
			return
		}
		// try every row in the next column
		for i := 0; i < n; i++ {
			if b.IsSafe(i, col) {
				// place a queen
				b.Place(i, col)
				// try next column
				backtracking(b, col+1, n)
				// remove a queen
				b.Remove(i, col)
			}
		}
	}

	backtracking(&board, 0, n)
	return result
}

// board class
type Board struct {
	M []string
	N int
}

func BoardConstructor(n int) Board {
	m := []string{}
	for i := 0; i < n; i++ {
		temp := ""
		for j := 0; j < n; j++ {
			temp += "."
		}
		m = append(m, temp)
	}
	return Board{m, n}
}

func (b *Board) Place(row, col int) {
	// it means b.M[row][col] = "Q"
	b.M[row] = b.M[row][:col] + "Q" + b.M[row][col+1:]
}

func (b *Board) Remove(row, col int) {
	// it means b.M[row][col] = "."
	b.M[row] = b.M[row][:col] + "." + b.M[row][col+1:]
}

func (b *Board) IsSafe(row, col int) bool {
	// check row and col
	for i := 0; i < b.N; i++ {
		if b.M[i][col] == 'Q' {
			return false
		}
		if b.M[row][i] == 'Q' {
			return false
		}
	}
	// check diagonal
	for i := 0; i < b.N; i++ {
		for j := 0; j < b.N; j++ {
			if i+j == row+col || i-j == row-col {
				if i != row && j != col && b.M[i][j] == 'Q' {
					return false
				}
			}
		}
	}
	return true
}

func (b *Board) Clone() []string {
	m := []string{}
	for i := 0; i < b.N; i++ {
		m = append(m, b.M[i])
	}
	return m
}

func main() {
	fmt.Println(solveNQueens(4))
}
