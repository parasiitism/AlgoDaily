package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sortedArrayToBST(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}
	return buildTree(nums, 0, len(nums)-1)
}

// idea: the mid of a sorted array is the parent of a sub tree
// 1,2,3
// 		2
//	1		3
func buildTree(nums []int, min int, max int) *TreeNode {
	if min > max {
		return nil
	}
	mean := (min + max) / 2
	node := &TreeNode{nums[mean], nil, nil}
	node.Left = buildTree(nums, min, mean-1)
	node.Right = buildTree(nums, mean+1, max)
	return node
}

func main() {

}
