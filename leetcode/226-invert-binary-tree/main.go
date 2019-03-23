package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	class approach: recursion

	Time  O(n)
	Space O(h)
	20 ms, faster than 69.85%
*/
func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	temp := root.Left
	root.Left = invertTree(root.Right)
	root.Right = invertTree(temp)
	return root
}

/*
	class approach: iterative bfs

	Time  O(n)
	Space O(1)
	0 ms, faster than 100.00%
*/
func invertTree1(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	q := []*TreeNode{}
	q = append(q, root)
	for len(q) > 0 {
		head := q[len(q)-1]
		q = q[:len(q)-1]
		head.Left, head.Right = head.Right, head.Left
		if head.Left != nil {
			q = append(q, head.Left)
		}
		if head.Right != nil {
			q = append(q, head.Right)
		}
	}
	return root
}

func main() {

}
