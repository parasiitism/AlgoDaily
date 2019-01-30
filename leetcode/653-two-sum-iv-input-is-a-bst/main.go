package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach
	1. dfs all the nodes, and put the node.val into a set
	2. if k-node.val exists in the set, return true
	Time		O(n)
	Space		O(n) hashtable, recursion
	32ms beats 50%
*/
func findTarget(root *TreeNode, k int) bool {
	ht := make(map[int]bool)
	return dfs(root, k, ht)
}

func dfs(node *TreeNode, k int, seen map[int]bool) bool {
	if node == nil {
		return false
	}
	if _, x := seen[k-node.Val]; x {
		return true
	}
	seen[node.Val] = true
	left := dfs(node.Left, k, seen)
	right := dfs(node.Right, k, seen)
	return left || right
}

/*
	2nd approach
	1. bfs all the nodes, and put the node.val into a set
	2. if k-node.val exists in the set, return true immediately
	Time		O(n)
	Space		O(n) hashtable
	32ms beats 50%
*/
func findTarget1(root *TreeNode, k int) bool {
	seen := make(map[int]bool)
	// bfs
	var queue []*TreeNode
	queue = append(queue, root)
	for len(queue) > 0 {
		n := len(queue)
		for i := 0; i < n; i++ {
			head := queue[0]
			queue = queue[1:]
			if _, x := seen[k-head.Val]; x {
				return true
			}
			seen[head.Val] = true
			if head.Left != nil {
				queue = append(queue, head.Left)
			}
			if head.Right != nil {
				queue = append(queue, head.Right)
			}
		}
	}
	return false
}

func main() {

}
