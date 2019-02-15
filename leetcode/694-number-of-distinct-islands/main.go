package main

import (
	"fmt"
	"math"
	"strconv"
)

/*
	1st approach
	- recursive dfs
	- translate the islands' coordinates, each island should start from 0,0
	 e.g. [(2, 3), (2, 4), (3, 4)] => [(0, 0), (0, 1), (1, 1)]
	- put the translated coordinates into a set

	i think the 2nd way is to do it with an iterative dfs

	Time    O(n*a) a: area of largest island
	Space   O(n) hashtable + itermediate result
	44 ms, faster than 75.00%
*/
func numDistinctIslands(grid [][]int) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
		return 0
	}
	// visited
	visited := [][]bool{}
	for i := 0; i < len(grid); i++ {
		temp := []bool{}
		for j := 0; j < len(grid[0]); j++ {
			temp = append(temp, false)
		}
		visited = append(visited, temp)
	}
	// curVisited
	curVisited := [][]int{}
	// top most, left most for key calculation
	curLeftMost := math.MaxInt64
	curTopMost := math.MaxInt64
	// dfs declaration
	var dfs func(i int, j int)
	dfs = func(i int, j int) {
		if i < 0 || i+1 > len(grid) || j < 0 || j+1 > len(grid[0]) || visited[i][j] == true {
			return
		}
		visited[i][j] = true
		if grid[i][j] == 1 {
			curVisited = append(curVisited, []int{i, j})
			if i < curTopMost {
				curTopMost = i
			}
			if j < curLeftMost {
				curLeftMost = j
			}
			dfs(i-1, j)
			dfs(i+1, j)
			dfs(i, j-1)
			dfs(i, j+1)
		}
	}
	resSet := make(map[string]bool)
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 1 {
				dfs(i, j)
				// calculate the key
				resKey := ""
				for _, o := range curVisited {
					row := o[0] - curTopMost
					col := o[1] - curLeftMost
					resKey += strconv.Itoa(row) + "," + strconv.Itoa(col) + "|"
				}
				if len(resKey) > 0 {
					resSet[resKey] = true
				}
				// reset
				curVisited = [][]int{}
				curLeftMost = math.MaxInt64
				curTopMost = math.MaxInt64
			} else {
				visited[i][j] = true
			}
		}
	}
	return len(resSet)
}

func main() {
	a := [][]int{
		{1, 1, 0, 0, 0},
		{1, 1, 0, 0, 0},
		{0, 0, 0, 1, 1},
		{0, 0, 0, 1, 1},
	}
	fmt.Println(numDistinctIslands(a))

	a = [][]int{
		{1, 1, 0, 1, 1},
		{1, 0, 0, 0, 0},
		{0, 0, 0, 0, 1},
		{1, 1, 0, 1, 1},
	}
	fmt.Println(numDistinctIslands(a))

	a = [][]int{
		{1, 1, 0},
		{0, 1, 1},
		{0, 0, 0},
		{1, 1, 1},
		{0, 1, 0},
	}
	fmt.Println(numDistinctIslands(a))
}
