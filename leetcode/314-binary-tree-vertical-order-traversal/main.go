package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type Item struct {
	Node *TreeNode
	Diff int
}

/*
	1st approach
	1. find the width of the binary tree, bfs recursively
	2. bfs the tree with a corresponding 'diff'
	3. put the node.val into a right subarray of result corresponding to the 'diff'

	Time    O(n)
	Space   O(h+n) the height of tree(recursion) + the result
	24ms beats 100%
*/
func verticalOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	// find the min & max
	min := 0
	max := 0
	var findWidth func(node *TreeNode, at int)
	findWidth = func(node *TreeNode, at int) {
		if node == nil {
			return
		}
		if at < min {
			min = at
		}
		if at > max {
			max = at
		}
		findWidth(node.Left, at-1)
		findWidth(node.Right, at+1)
	}
	findWidth(root, 0)

	// create an empty result array
	n := max - min + 1
	res := [][]int{}
	for i := 0; i < n; i++ {
		res = append(res, []int{})
	}
	// bfs the tree the put values into the right subarraries
	var q []Item
	q = append(q, Item{root, 0})
	for len(q) > 0 {
		item := q[0]
		q = q[1:]
		node := item.Node
		diff := item.Diff
		res[diff-min] = append(res[diff-min], node.Val)
		if node.Left != nil {
			q = append(q, Item{node.Left, diff - 1})
		}
		if node.Right != nil {
			q = append(q, Item{node.Right, diff + 1})
		}
	}
	return res
}

/*
	2nd approach
	1. find the width of the binary tree, bfs iteratively
	2. bfs the tree with a corresponding 'diff'
	3. put the node.val into a right subarray of result corresponding to the 'diff'

	Time    O(n)
	Space   O(h+n) the height of tree(recursion) + the result
	24ms beats 100%
*/
func verticalOrder1(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	// find the min & max
	min := 0
	max := 0
	var s []Item
	s = append(s, Item{root, 0})
	for len(s) > 0 {
		item := s[len(s)-1]
		s = s[:len(s)-1]
		node := item.Node
		diff := item.Diff
		if diff < min {
			min = diff
		}
		if diff > max {
			max = diff
		}
		if node.Left != nil {
			s = append(s, Item{node.Left, diff - 1})
		}
		if node.Right != nil {
			s = append(s, Item{node.Right, diff + 1})
		}
	}

	// create an empty result array
	n := max - min + 1
	res := [][]int{}
	for i := 0; i < n; i++ {
		res = append(res, []int{})
	}
	// bfs the tree the put values into the right subarraries
	var q []Item
	q = append(q, Item{root, 0})
	for len(q) > 0 {
		item := q[0]
		q = q[1:]
		node := item.Node
		diff := item.Diff
		res[diff-min] = append(res[diff-min], node.Val)
		if node.Left != nil {
			q = append(q, Item{node.Left, diff - 1})
		}
		if node.Right != nil {
			q = append(q, Item{node.Right, diff + 1})
		}
	}
	return res
}

func main() {
	// 		1
	//	2		3
	// 4 5 6 7
	//			8
	root := &TreeNode{1,
		&TreeNode{2,
			&TreeNode{4, nil, nil},
			&TreeNode{5, nil, nil},
		},
		&TreeNode{3,
			&TreeNode{6,
				nil,
				&TreeNode{8, nil, nil},
			},
			&TreeNode{7, nil, nil},
		},
	}
	// print 1234567
	fmt.Println(verticalOrder(root))
	fmt.Println(verticalOrder1(root))
}
