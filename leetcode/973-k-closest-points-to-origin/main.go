package main

import (
	"fmt"
	"sort"
)

/*
	1st approach
	- calculate all the points distance
	- sort the result
	Time		O(nlogn)
	Space		O(n) points' distance
	688ms beats 72.46%
	25jan2019
*/
type Point struct {
	Dist int
	Coor []int
}

func kClosest(points [][]int, K int) [][]int {
	dists := []Point{}
	for i := 0; i < len(points); i++ {
		point := points[i]
		dist := point[0]*point[0] + point[1]*point[1]
		dists = append(dists, Point{dist, point})
	}
	sort.Slice(dists, func(i, j int) bool {
		return dists[i].Dist < dists[j].Dist
	})
	res := [][]int{}
	for i := 0; i < len(points) && i < K; i++ {
		res = append(res, dists[i].Coor)
	}
	return res
}

/*
	another approach:
	- calculate all the points distance
	- put them into a BST
	- the result is the first k element of the BST inorder traversal
	Time		O(nlogn)
	Space		O(n)
	i am not gonna implement because it is too tedious
*/

func main() {
	a := [][]int{
		{1, 3},
		{-2, 2},
	}
	fmt.Println(kClosest(a, 1))

	a = [][]int{
		{1, 3},
		{-2, 2},
	}
	fmt.Println(kClosest(a, 3))

	a = [][]int{
		{3, 3},
		{5, -1},
		{-2, 4},
	}
	fmt.Println(kClosest(a, 2))
}
