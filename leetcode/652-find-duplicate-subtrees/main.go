package main

import (
	"strconv"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach: recursive dfs + hashtable + set
	1. traverse the tree and use a hashtable cache the tree structure as a string, preorder/postorder but not inorder(will be duplicate)
	2. during the traversal, if we found a duplicate key in the hashtable, put the tree into the set
	3. the result is the corresponding trees of the keys in the set

	Time		O(n) traverse all the nodes
	Space		O(h+n) h: height of tree, n: number of nodes
	28 ms, faster than 43.10%
*/
func findDuplicateSubtrees(root *TreeNode) []*TreeNode {
	m := make(map[string]*TreeNode)
	dup := make(map[string]bool)
	// dfs
	var dfs func(node *TreeNode) string
	dfs = func(node *TreeNode) string {
		if node == nil {
			return "*"
		}
		left := dfs(node.Left)
		right := dfs(node.Right)
		// cache the structure of the tree, preorder/postoder sequence
		// for inorder, there will be a duplicate for diff structures
		key := left + "," + right + "<" + strconv.Itoa(node.Val) + ">"
		if _, x := m[key]; x {
			// if seen, put the key into the set
			dup[key] = true
		} else {
			m[key] = node
		}
		return key
	}
	dfs(root)
	// the result are the subtrees corresponding to the keys in the set
	res := []*TreeNode{}
	for key := range dup {
		res = append(res, m[key])
	}
	return res
}

func main() {

}
