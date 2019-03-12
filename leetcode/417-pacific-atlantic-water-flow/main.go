package main

import (
	"fmt"
)

/*
	1st approach:
	- for each node, bfs to see if it can reach the boundaries

	Time	O(n^2)
	Space	O(n)
	n = row * col
	3248 ms, faster than 11.11%
*/
func pacificAtlantic(matrix [][]int) [][]int {
	res := [][]int{}
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[0]); j++ {
			a, b := bfs(i, j, matrix)
			if a && b {
				res = append(res, []int{i, j})
			}
		}
	}
	return res
}

func bfs(fromI, fromJ int, matrix [][]int) (bool, bool) {
	reachP := false
	reachA := false

	// visited
	visited := [][]bool{}
	for i := 0; i < len(matrix); i++ {
		temp := []bool{}
		for j := 0; j < len(matrix[i]); j++ {
			temp = append(temp, false)
		}
		visited = append(visited, temp)
	}
	// bfs
	q := [][]int{}
	q = append(q, []int{fromI, fromJ, matrix[fromI][fromJ]})
	for len(q) > 0 {
		head := q[0]
		i, j, h := head[0], head[1], head[2]
		q = q[1:]

		if i == -1 && j >= 0 && j < len(matrix[0]) {
			reachP = true
			continue
		}

		if i == len(matrix) && j >= 0 && j < len(matrix[0]) {
			reachA = true
			continue
		}

		if j == -1 && i >= 0 && i < len(matrix) {
			reachP = true
			continue
		}

		if j == len(matrix[0]) && i >= 0 && i < len(matrix) {
			reachA = true
			continue
		}

		if matrix[i][j] <= h {
			if visited[i][j] {
				continue
			}
			visited[i][j] = true
			q = append(q, []int{i - 1, j, matrix[i][j]})
			q = append(q, []int{i + 1, j, matrix[i][j]})
			q = append(q, []int{i, j - 1, matrix[i][j]})
			q = append(q, []int{i, j + 1, matrix[i][j]})
		}
	}
	return reachP, reachA
}

func main() {
	a := [][]int{
		{1, 2, 2, 3, 5},
		{3, 2, 3, 4, 4},
		{2, 4, 5, 3, 1},
		{6, 7, 1, 4, 5},
		{5, 1, 1, 2, 4},
	}
	fmt.Println(pacificAtlantic(a))

	a = [][]int{
		{1, 2, 2, 3, 5},
		{3, 1, 1, 4, 4},
		{2, 1, 3, 3, 1},
		{6, 1, 9, 9, 9},
		{5, 1, 1, 1, 1},
		{5, 9, 9, 9, 9},
	}
	fmt.Println(pacificAtlantic(a))
}
