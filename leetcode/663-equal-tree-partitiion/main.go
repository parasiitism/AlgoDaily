package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach: dfs + hashtable
	- for each node, calculate its children sum
	- calculate the total sum as well
	- dfs again to check if total - cur == cur

	corner cases:
	- [0,null,0]
	- [0,-1,1]

	20 ms, faster than 83.33%
*/
func checkEqualTree(root *TreeNode) bool {
	if root == nil {
		return false
	}
	m := make(map[*TreeNode]int)
	total := calSum(root, m)

	stack := []*TreeNode{root}
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if pop != root && total == 2*m[pop] {
			return true
		}
		if pop.Left != nil {
			stack = append(stack, pop.Left)
		}
		if pop.Right != nil {
			stack = append(stack, pop.Right)
		}
	}
	return false
}

func calSum(node *TreeNode, m map[*TreeNode]int) int {
	if node == nil {
		return 0
	}
	left := calSum(node.Left, m)
	right := calSum(node.Right, m)
	sum := left + node.Val + right
	m[node] = sum
	return sum
}

/*
	2nd approach: dfs + hashset, learned from others
	- for each node, calculate its children sum
	- calculate the total sum as well
	- dfs again to check if total - cur == cur

	compare to the 1st approach:
	- actually we dont need to care if there are duplicate sum values,
	because if there are, lets say 2 same values , it means that we can cut the tree in 2 ways

	ref:
	- https://leetcode.com/problems/equal-tree-partition/discuss/106727/javac-simple-solution-with-only-one-hashmap

	corner cases:
	- [0,null,0]
	- [0,-1,1]

	32 ms, faster than 16.67%
*/
func checkEqualTree1(root *TreeNode) bool {
	if root == nil {
		return false
	}
	m := make(map[int]bool)
	total := root.Val + calSum1(root.Left, m) + calSum1(root.Right, m)
	// check if total is even
	if total%2 != 0 {
		return false
	}
	if _, x := m[total/2]; x {
		return true
	}
	return false
}

func calSum1(node *TreeNode, m map[int]bool) int {
	if node == nil {
		return 0
	}
	left := calSum1(node.Left, m)
	right := calSum1(node.Right, m)
	sum := left + node.Val + right
	m[sum] = true
	return sum
}

func main() {

}
