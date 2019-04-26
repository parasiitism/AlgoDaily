package main

import (
	"fmt"
	"math"
)

/*
	1st approach: dfs

	Time	O(N)
	Space	O(h)
*/
func wallsAndGates(rooms [][]int) {
	for i := 0; i < len(rooms); i++ {
		for j := 0; j < len(rooms[0]); j++ {
			if rooms[i][j] == 0 {
				// to speed up the calculation
				// instead of calculating from the INF, calculating from 0 can avoid redundant calculation
				dfs(rooms, i, j, 0)
			}
		}
	}
}

func dfs(rooms [][]int, i int, j int, steps int) {
	if i < 0 || i+1 > len(rooms) || j < 0 || j+1 > len(rooms[0]) {
		return
	}
	if rooms[i][j] == -1 {
		return
	}
	// if the "steps" is calculated, dont need to calculate again
	if steps <= rooms[i][j] {
		rooms[i][j] = steps
		dfs(rooms, i-1, j, steps+1)
		dfs(rooms, i+1, j, steps+1)
		dfs(rooms, i, j-1, steps+1)
		dfs(rooms, i, j+1, steps+1)
	}
}

func main() {
	inf := math.MaxInt32
	fmt.Println(inf)
	mapp := [][]int{
		{inf, -1, 0, inf},
		{inf, inf, inf, -1},
		{inf, -1, inf, -1},
		{0, -1, inf, inf},
	}
	wallsAndGates(mapp)
	fmt.Println(mapp)
}
