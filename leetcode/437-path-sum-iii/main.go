package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach:
	- memorize the sum of all subpaths on each node
	- TLE
	Time O(n^2)
	Space...a lot
	14jan2019
*/
func pathSum_(root *TreeNode, sum int) int {
	res := 0
	var dfs func(node *TreeNode, agg []SumNode)
	dfs = func(node *TreeNode, agg []SumNode) {
		if node == nil {
			return
		}
		newAgg := []SumNode{}
		for i := 0; i < len(agg); i++ {
			newPath := []int{}
			newPath = append(newPath, agg[i].Paths...)
			newPath = append(newPath, node.Val)
			newSum := agg[i].Sum + node.Val
			newAgg = append(newAgg, SumNode{newPath, newSum})
			if newSum == sum {
				res++
			}
		}
		newAgg = append(newAgg, SumNode{[]int{node.Val}, node.Val})
		if node.Val == sum {
			res++
		}
		dfs(node.Left, newAgg)
		dfs(node.Right, newAgg)
	}
	dfs(root, []SumNode{})
	return res
}

type SumNode struct {
	Paths []int
	Sum   int
}

/*
	2nd approach:
	- optimize the above one
	e.g. for path [10, 5, 2, 1], for each node 10 -> [10], 5 -> [15,5], 2 -> [17,7,2], 1 -> [18,8,3,1]
	Time		O(n^2)
	Space		O(n^2)
	24ms beats 28.57%
	14jan2019
*/
func pathSum(root *TreeNode, sum int) int {
	res := 0
	var dfs func(node *TreeNode, agg []int)
	dfs = func(node *TreeNode, agg []int) {
		if node == nil {
			return
		}
		newAgg := []int{}
		for i := 0; i < len(agg); i++ {
			temp := agg[i] + node.Val
			newAgg = append(newAgg, temp)
			if temp == sum {
				res++
			}
		}
		newAgg = append(newAgg, node.Val)
		if node.Val == sum {
			res++
		}
		dfs(node.Left, newAgg)
		dfs(node.Right, newAgg)
	}
	dfs(root, []int{})
	return res
}

func main() {
	// 			10
	//		5		-3
	// 3	 2	  11
	//3 -2  1
	root := &TreeNode{10,
		&TreeNode{5,
			&TreeNode{3,
				&TreeNode{3,
					nil,
					nil,
				},
				&TreeNode{-2,
					nil,
					nil,
				},
			},
			&TreeNode{2,
				nil,
				&TreeNode{1,
					nil,
					nil,
				},
			},
		},
		&TreeNode{-3,
			nil,
			&TreeNode{11,
				nil,
				nil,
			},
		},
	}
	fmt.Println(pathSum(root, 8))
}
