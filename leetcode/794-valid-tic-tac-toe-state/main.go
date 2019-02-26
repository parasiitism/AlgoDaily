package main

import "fmt"

/*
	1st approach: very stupid checking

	Time	O(1) since board size is fixed
	Space	O(1) since board size is fixed
	0 ms, faster than 100.00%
*/
func validTicTacToe(board []string) bool {
	nx := 0
	no := 0
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			if board[i][j] == 'X' {
				nx++
			}
			if board[i][j] == 'O' {
				no++
			}
		}
	}
	if no > nx {
		return false
	} else if nx > no+1 {
		return false
	}
	winCountX := 0
	winCountO := 0
	// check rows and columns
	rowCountX := []int{0, 0, 0}
	colCountX := []int{0, 0, 0}
	rowCountO := []int{0, 0, 0}
	colCountO := []int{0, 0, 0}
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if board[i][j] == 'X' {
				rowCountX[i]++
				if rowCountX[i] == 3 {
					winCountX++
				}
				colCountX[j]++
				if colCountX[j] == 3 {
					winCountX++
				}
			}
			if board[i][j] == 'O' {
				rowCountO[i]++
				if rowCountO[j] == 3 {
					winCountO++
				}
				colCountO[j]++
				if colCountO[j] == 3 {
					winCountO++
				}
			}
		}
	}
	diagCountX := 0
	diagCountO := 0
	for i := 0; i < 3; i++ {
		if board[i][i] == 'X' {
			diagCountX++
			if diagCountX == 3 {
				winCountX++
			}
		}
		if board[i][i] == 'O' {
			diagCountO++
			if diagCountO == 3 {
				winCountO++
			}
		}
	}
	antiDiagCountX := 0
	antiDiagCountO := 0
	for i := 2; i >= 0; i-- {
		if board[i][2-i] == 'X' {
			antiDiagCountX++
			if antiDiagCountX == 3 {
				winCountX++
			}
		}
		if board[i][2-i] == 'O' {
			antiDiagCountO++
			if antiDiagCountO == 3 {
				winCountO++
			}
		}
	}
	if winCountX == 0 && winCountO == 0 {
		return true
	} else if winCountX == 0 && winCountO > 0 {
		if no < nx {
			return false
		}
		return true
	} else if winCountX > 0 && winCountO == 0 {
		if no == nx {
			return false
		}
		return true
	}
	return false
}

func main() {
	a := []string{
		"O  ", "   ", "   ",
	}
	fmt.Println(validTicTacToe(a))

	a = []string{
		"XOX", " X ", "   ",
	}
	fmt.Println(validTicTacToe(a))

	a = []string{
		"XXX", "   ", "OOO",
	}
	fmt.Println(validTicTacToe(a))

	a = []string{
		"XOX", "O O", "XOX",
	}
	fmt.Println(validTicTacToe(a))

	a = []string{
		"XXX", "OOX", "OOX",
	}
	fmt.Println(validTicTacToe(a))

	a = []string{
		"XXX", "XOO", "OO ",
	}
	fmt.Println(validTicTacToe(a))

	a = []string{
		"XXO", "XOX", "OXO",
	}
	fmt.Println(validTicTacToe(a))
}
