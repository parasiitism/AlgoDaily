package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	naive approach
	1. dfs all the nodes, and put the node.val into an array
	2. remove duplicates from array
	3. sort the array and return the 2nd item
	Time O(nlogn)
	Space		O(n) hashtable, recursion
	not gonna implement
*/

/*
	1st approach
	1. dfs all the nodes, and put the node.val into a set
	2. get the 2nd min val by traversing the set
	Time		O(n)
	Space		O(n) hashtable, recursion
	0ms beats 100%
*/
func findSecondMinimumValue(root *TreeNode) int {
	ht := make(map[int]bool)
	dfs(root, ht)
	min := math.MaxInt64
	min2 := math.MaxInt64
	for k, _ := range ht {
		if k < min {
			min2 = min
			min = k
		} else if k < min2 {
			min2 = k
		}
	}
	if min2 == math.MaxInt64 {
		return -1
	}
	return min2
}

func dfs(node *TreeNode, seen map[int]bool) {
	if node == nil {
		return
	}
	seen[node.Val] = true
	dfs(node.Left, seen)
	dfs(node.Right, seen)
}

/*
	2nd approach
	1. bfs all the nodes, and put the node.val into a set
	2. get the 2nd min val by traversing the set
	Time		O(n)
	Space		O(n) hashtable
	0ms beats 100%
*/
func findSecondMinimumValue1(root *TreeNode) int {
	seen := make(map[int]bool)
	// bfs
	var queue []*TreeNode
	queue = append(queue, root)
	for len(queue) > 0 {
		n := len(queue)
		for i := 0; i < n; i++ {
			head := queue[0]
			queue = queue[1:]
			seen[head.Val] = true
			if head.Left != nil {
				queue = append(queue, head.Left)
			}
			if head.Right != nil {
				queue = append(queue, head.Right)
			}
		}
	}
	// find 2nd min
	min := math.MaxInt64
	min2 := math.MaxInt64
	for k, _ := range seen {
		if k < min {
			min2 = min
			min = k
		} else if k < min2 {
			min2 = k
		}
	}
	if min2 == math.MaxInt64 {
		return -1
	}
	return min2
}

func main() {

	// 			  2
	//	  2			 3
	// 4   5 		8
	//6 7
	root := &TreeNode{2,
		&TreeNode{2,
			&TreeNode{4,
				&TreeNode{6, nil, nil},
				&TreeNode{7, nil, nil},
			},
			&TreeNode{5, nil, nil},
		},
		&TreeNode{3,
			&TreeNode{8, nil, nil},
			nil,
		},
	}
	fmt.Println(findSecondMinimumValue(root))

	// 			  2
	//	  2			 3
	// 4   5 		8
	//6 7
	root := &TreeNode{2,
		&TreeNode{2,
			&TreeNode{4,
				&TreeNode{6, nil, nil},
				&TreeNode{7, nil, nil},
			},
			&TreeNode{5, nil, nil},
		},
		&TreeNode{3,
			&TreeNode{8, nil, nil},
			nil,
		},
	}
	fmt.Println(findSecondMinimumValue(root))
}
