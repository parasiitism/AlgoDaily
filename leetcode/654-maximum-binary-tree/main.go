package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	Questions to ask:
	- duplicate values?
	- negative values?
*/

/*
	1st aproach
	1. find the max
	2. set the node with max value
	3. set the node.left with nums[:i] and node.right with nums[i+1:] recursively
	Time	O(n)
	Space	O(h)
	68ms beats 100%
	30jan2019
*/
func constructMaximumBinaryTree(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}
	i := findMax(nums)
	root := &TreeNode{nums[i], nil, nil}
	root.Left = constructMaximumBinaryTree(nums[:i])
	root.Right = constructMaximumBinaryTree(nums[i+1:])
	return root
}

func findMax(nums []int) int {
	max := nums[0]
	idx := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] > max {
			max = nums[i]
			idx = i
		}
	}
	return idx
}

/*
	2nd aproach
	- same logic but put the findMax() in the function to reduce stack allocation time
	Time	O(n)
	Space	O(h)
	68ms beats 100%
	30jan2019
*/
func constructMaximumBinaryTree1(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}

	max := nums[0]
	idx := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] > max {
			max = nums[i]
			idx = i
		}
	}

	root := &TreeNode{nums[idx], nil, nil}
	root.Left = constructMaximumBinaryTree(nums[:idx])
	root.Right = constructMaximumBinaryTree(nums[idx+1:])
	return root
}

func main() {

}
