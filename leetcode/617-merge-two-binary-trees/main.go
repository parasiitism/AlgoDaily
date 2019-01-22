package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st attempt
	- dfs all the nodes, sum the result
	Time	O(n)
	Space O(max(h))
	40ms beats 59.15%
	22jan2019
*/
func mergeTrees(t1 *TreeNode, t2 *TreeNode) *TreeNode {
	if t1 == nil && t2 == nil {
		return nil
	}

	node := &TreeNode{0, nil, nil}

	sum := 0
	if t1 != nil {
		sum += t1.Val
	}
	if t2 != nil {
		sum += t2.Val
	}

	node.Val = sum

	var left1 *TreeNode
	var left2 *TreeNode
	var right1 *TreeNode
	var right2 *TreeNode
	if t1 != nil && t2 != nil {
		left1, left2 = t1.Left, t2.Left
		right1, right2 = t1.Right, t2.Right
	} else if t1 != nil {
		left1, right1 = t1.Left, t1.Right
	} else if t2 != nil {
		left2, right2 = t2.Left, t2.Right
	}

	node.Left = mergeTrees(left1, left2)
	node.Right = mergeTrees(right1, right2)

	return node
}

/*
	2nd attempt
	- same as above
	- simplify the logic
	Time	O(n)
	Space O(max(h))
	36ms beats 100%
	22jan2019
*/
func mergeTrees1(t1 *TreeNode, t2 *TreeNode) *TreeNode {
	if t1 == nil {
		return t2
	}
	if t2 == nil {
		return t1
	}
	node := &TreeNode{t1.Val + t2.Val, nil, nil}
	node.Left = mergeTrees(t1.Left, t2.Left)
	node.Right = mergeTrees(t1.Right, t2.Right)
	return node
}

func main() {

}
