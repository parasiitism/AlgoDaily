package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach: bottom-up recursion, learned from others
	- for each node, we can decide whether we should rob this house, 2 options: rob or not rob
	- basically if we do top-down, we pass down 2 options to it children,
		but we might need to change the visited paths because we need to ensure that we dont rob adjacent houses along a path
	- therefore we should do it with bottom-up approach
	- for each node, we return (rob, notrob) back to its parent
	- a parent should add up the lucre or not and return back to its parent
		e.g. for each node,
		rob := node.Val + leftNotRob + rightNotRob
		notRob := max(leftRob, leftNotRob) + max(rightRob, rightNotRob)
	- the base case of the recursion is (0,0) when the node == nil

	ref:
	- learned from https://www.youtube.com/watch?v=-i2BFAU25Zk

	Time		O(n)
	Space		O(h) -> O(n)
	4 ms, faster than 100.00%
*/

func rob(root *TreeNode) int {
	rob, notRob := helper(root)
	return max(rob, notRob)
}

func helper(node *TreeNode) (int, int) {
	if node == nil {
		return 0, 0
	}
	leftRob, leftNotRob := helper(node.Left)
	rightRob, rightNotRob := helper(node.Right)
	thisRob := node.Val + leftNotRob + rightNotRob
	thisNotRob := max(leftRob, leftNotRob) + max(rightRob, rightNotRob)
	return thisRob, thisNotRob
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {

}
