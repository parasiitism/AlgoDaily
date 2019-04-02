package main

import "sort"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type Item struct {
	Val int
	Row int
}

/*
	2nd approach: dfs + hashtable

	this is a very weird question, the nodes on the same level(level order) are asked to be sorted

	Time    O(n)
	Space   O(n)
	0 ms, faster than 100.00%
*/
func verticalTraversal(root *TreeNode) [][]int {
	ht := make(map[int][]Item)

	// left most col
	leftMostCol := 0

	// dfs
	var dfs func(node *TreeNode, col int, row int)
	dfs = func(node *TreeNode, col int, row int) {
		if node == nil {
			return
		}
		ht[col] = append(ht[col], Item{node.Val, row})
		if col < leftMostCol {
			leftMostCol = col
		}
		dfs(node.Left, col-1, row+1)
		dfs(node.Right, col+1, row+1)
	}
	dfs(root, 0, 0)

	// construct result
	res := [][]int{}
	for true {
		if v, x := ht[leftMostCol]; x {
			// comparoter sort.Slice
			// sort by colLevel, order numerically if tie
			sort.Slice(v, func(i, j int) bool {
				if v[i].Row < v[j].Row {
					return true
				} else if v[i].Row > v[j].Row {
					return false
				} else {
					return v[i].Val < v[j].Val
				}
			})
			trim := []int{}
			for _, x := range v {
				trim = append(trim, x.Val)
			}
			res = append(res, trim)
			leftMostCol++
		} else {
			break
		}
	}
	return res
}

func main() {

}
