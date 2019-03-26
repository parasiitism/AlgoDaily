package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach:
	1. dfs to count the depth for each leafs
	2. compare the depths and check if there are increasing or depths+1<maxdepth

	e.g.1
				1
			2		3
		4 5	 6
	the depths are [3,3,3,2], which is a complets tree

	e.g.2
				1
			2		3
		4 5	 	6
	the depths are [3,3,2,3], which is not a complets tree

	Time	O(2n)
	Space	O(h)
	0 ms, faster than 100.00%
*/
func isCompleteTree(root *TreeNode) bool {
	if root == nil {
		return true
	}
	arr := []int{}
	var dfs func(node *TreeNode, cnt int)
	dfs = func(node *TreeNode, cnt int) {
		if node.Left == nil && node.Right == nil {
			arr = append(arr, cnt)
		} else if node.Left == nil {
			arr = append(arr, cnt)
			dfs(node.Right, cnt+1)
		} else if node.Right == nil {
			dfs(node.Left, cnt+1)
			arr = append(arr, cnt)
		} else {
			dfs(node.Left, cnt+1)
			dfs(node.Right, cnt+1)
		}
	}
	dfs(root, 1)

	depth := arr[0]
	prev := arr[0]
	for i := 1; i < len(arr); i++ {
		num := arr[i]
		/*
			check depths difference
			- no increasing
			- no larger than the depth from left
			- no different more than 1
		*/
		if num > depth || num > prev || num+1 < depth {
			return false
		}
		prev = num
	}
	return true
}

func main() {

}
