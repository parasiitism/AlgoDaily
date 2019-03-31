package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach: recursive dfs

	Time		O(n)
	Space		O(h)
	0 ms, faster than 100.00%
*/
func sumOfLeftLeaves(root *TreeNode) int {
	return helper(root, false)
}

func helper(node *TreeNode, isLeft bool) int {
	if node == nil {
		return 0
	}
	if node.Left == nil && node.Right == nil {
		if isLeft == true {
			return node.Val
		} else {
			return 0
		}
	}
	left := helper(node.Left, true)
	right := helper(node.Right, false)
	return left + right
}

/*
	2nd approach: iterative dfs

	Time		O(n)
	Space		O(h)
	0 ms, faster than 100.00%
*/

type StackItem struct {
	Node   *TreeNode
	IsLeft bool
}

func sumOfLeftLeaves1(root *TreeNode) int {
	if root == nil {
		return 0
	}
	res := 0
	stack := []*StackItem{}
	stack = append(stack, &StackItem{root, false})
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		// check and increment result
		if pop.Node.Left == nil && pop.Node.Right == nil {
			if pop.IsLeft == true {
				res += pop.Node.Val
			}
		}
		// append children into stack
		if pop.Node.Left != nil {
			stack = append(stack, &StackItem{pop.Node.Left, true})
		}
		if pop.Node.Right != nil {
			stack = append(stack, &StackItem{pop.Node.Right, false})
		}
	}
	return res
}

func main() {

}
