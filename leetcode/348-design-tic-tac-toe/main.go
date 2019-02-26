package main

import "fmt"

/*
	1st approach:
	1. similar to leetcode 531, Lonely Pixel I, check the rows and columns by counting the occurence
	2. check diagonal grids as well

	Time		O(n)
	Space		O(n)
	392 ms, faster than 24.00%
*/

type TicTacToe struct {
	Board [][]int
	N     int
}

/** Initialize your data structure here. */
func Constructor(n int) TicTacToe {
	a := [][]int{}
	for i := 0; i < n; i++ {
		temp := []int{}
		for j := 0; j < n; j++ {
			temp = append(temp, 0)
		}
		a = append(a, temp)
	}
	return TicTacToe{a, n}
}

/** Player {player} makes a move at ({row}, {col}).
  @param row The row of the board.
  @param col The column of the board.
  @param player The player, can be either 1 or 2.
  @return The current winning condition, can be either:
          0: No one wins.
          1: Player 1 wins.
          2: Player 2 wins. */
func (this *TicTacToe) Move(row int, col int, player int) int {
	this.Board[row][col] = player
	// only the current player can win actually
	if this.check(player) == true {
		return player
	}
	return 0
}

func (this *TicTacToe) check(player int) bool {
	// check rows and columns
	rowCount := []int{}
	for i := 0; i < this.N; i++ {
		rowCount = append(rowCount, 0)
	}
	colCount := []int{}
	for i := 0; i < this.N; i++ {
		colCount = append(colCount, 0)
	}
	for i := 0; i < this.N; i++ {
		for j := 0; j < this.N; j++ {
			if this.Board[i][j] == player {
				rowCount[i]++
				if rowCount[i] == this.N {
					return true
				}
				colCount[j]++
				if colCount[j] == this.N {
					return true
				}
			}
		}
	}
	// check diagonals
	diagCount := 0
	for i := 0; i < this.N; i++ {
		if this.Board[i][i] == player {
			diagCount++
			if diagCount == this.N {
				return true
			}
		}
	}
	diagCount = 0
	for i := this.N - 1; i >= 0; i-- {
		if this.Board[i][this.N-i-1] == player {
			diagCount++
			if diagCount == this.N {
				return true
			}
		}
	}
	return false
}

func main() {
	obj := Constructor(3)
	fmt.Println(obj.Move(0, 0, 1))
	fmt.Println(obj.Move(0, 2, 2))
	fmt.Println(obj.Move(2, 2, 1))
	fmt.Println(obj.Move(1, 1, 2))
	fmt.Println(obj.Move(2, 0, 1))
	fmt.Println(obj.Move(1, 0, 2))
	fmt.Println(obj.Move(2, 1, 1))
}
