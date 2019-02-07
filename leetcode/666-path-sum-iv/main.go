package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st very stupid approach
	1. create a full binary tree with 4 storeies by dfs
	2. assign values to the nodes by bfs
	3. create a new tree with valid nodes by dfs
	4. calculate the path sum by dfs

	Time	O(4n)
	Space	O(n)
	7feb2019
*/
func pathSum(nums []int) int {
	// dfs to contruct an empty tree
	t := dfs(0, 4)
	var q []*TreeNode
	q = append(q, t)
	// bfs to assign values into the nodes
	level := 0
	for len(q) > 0 {
		n := len(q)
		for i := 0; i < n; i++ {
			head := q[0]
			q = q[1:len(q)]
			if len(nums) > 0 {
				pop := nums[0]
				a, b, c := decode(pop)
				if level+1 == a && i+1 == b {
					head.Val = c
					nums = nums[1:]
				}
			}
			if head.Left != nil {
				q = append(q, head.Left)
			}
			if head.Right != nil {
				q = append(q, head.Right)
			}
		}
		level++
	}
	// remove -1 node
	t = create(t)
	// bfs(t)
	// cal path sum
	res := 0
	var calSum func(node *TreeNode, sum int)
	calSum = func(node *TreeNode, sum int) {
		if node == nil {
			return
		}
		if node.Left == nil && node.Right == nil {
			res += sum + node.Val
		}
		calSum(node.Left, sum+node.Val)
		calSum(node.Right, sum+node.Val)
	}
	calSum(t, 0)

	return res
}

func decode(x int) (int, int, int) {
	nums := []int{}
	for x > 0 {
		nums = append(nums, x%10)
		x /= 10
	}
	return nums[2], nums[1], nums[0]
}

func dfs(storey int, k int) *TreeNode {
	node := &TreeNode{-1, nil, nil}
	if storey+1 < k {
		node.Left = dfs(storey+1, k)
		node.Right = dfs(storey+1, k)
	}
	return node
}

func create(node *TreeNode) *TreeNode {
	if node == nil || node.Val == -1 {
		return nil
	}
	newNode := &TreeNode{node.Val, nil, nil}
	newNode.Left = create(node.Left)
	newNode.Right = create(node.Right)
	return newNode
}

// print tree
func bfs(root *TreeNode) {
	var queue []*TreeNode
	queue = append(queue, root)
	for len(queue) > 0 {
		n := len(queue)
		for i := 0; i < n; i++ {
			head := queue[0]
			queue = queue[1:]
			fmt.Println(head.Val)
			if head.Left != nil {
				queue = append(queue, head.Left)
			}
			if head.Right != nil {
				queue = append(queue, head.Right)
			}
		}
	}
}

func main() {
	// 		5
	//	2		8
	// 1 3 7 9
	// root := &TreeNode{5,
	// 	&TreeNode{2,
	// 		&TreeNode{1, nil, nil},
	// 		&TreeNode{3, nil, nil},
	// 	},
	// 	&TreeNode{8,
	// 		&TreeNode{7, nil, nil},
	// 		&TreeNode{9, nil, nil},
	// 	},
	// }
	// fmt.Println(root)

	ans := pathSum([]int{115, 212, 228, 313, 323, 337, 349})
	fmt.Println(ans)

	ans = pathSum([]int{113, 215, 221})
	fmt.Println(ans)

	ans = pathSum([]int{113, 221})
	fmt.Println(ans)
}
