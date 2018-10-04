package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// this was my first attempt, iterative, un-optimized
// , but still beated 44% submissions Oct 3rd 2018
func deleteNode(root *TreeNode, key int) *TreeNode {
	// search
	var parent *TreeNode
	var direction int // 0,1
	curr := root
	for curr != nil && curr.Val != key {
		if key > curr.Val {
			parent = curr
			direction = 1
			curr = curr.Right
		} else {
			parent = curr
			direction = 0
			curr = curr.Left
		}
	}
	if curr == nil {
		return root
	}

	// target found
	// case 1: 0 child: remove the current node from its parent
	// case 2: 1 child: replace the current node with its child
	// case 3: 2 children: replace the current node with its in-order successor child
	// for detail: read ./delete_node_bst.png
	if curr.Left == nil && curr.Right == nil { // case A
		if parent == nil {
			return nil
		} else {
			if direction == 0 {
				parent.Left = nil
			} else {
				parent.Right = nil
			}
		}
	} else if curr.Left != nil && curr.Right == nil { // case 2A
		if parent == nil {
			return curr.Left
		} else {
			if direction == 0 {
				parent.Left = curr.Left
			} else {
				parent.Right = curr.Left
			}
		}
	} else if curr.Left == nil && curr.Right != nil { // case 2B
		if parent == nil {
			return curr.Right
		} else {
			if direction == 0 {
				parent.Left = curr.Right
			} else {
				parent.Right = curr.Right
			}
		}
	} else { // case 3
		if parent == nil {
			var successorParent *TreeNode
			successor := curr.Right
			for true {
				if successor.Left != nil {
					successorParent = successor
					successor = successor.Left
				} else {
					break
				}
			}
			successor.Left = curr.Left
			if successorParent != nil {
				successorParent.Left = successor.Right
				successor.Right = curr.Right
			}
			return successor
		} else {
			var successorParent *TreeNode
			successor := curr.Right
			for true {
				if successor.Left != nil {
					successorParent = successor
					successor = successor.Left
				} else {
					break
				}
			}
			if direction == 0 {
				successor.Left = curr.Left
				if successorParent != nil {
					successorParent.Left = successor.Right
					successor.Right = curr.Right
				}
				parent.Left = successor
			} else {
				successor.Left = curr.Left
				if successorParent != nil {
					successorParent.Left = successor.Right
					successor.Right = curr.Right
				}
				parent.Right = successor
			}
		}
	}

	return root
}

// suggested solution, recursive
//
func deleteNode1(root *TreeNode, key int) *TreeNode {
	if root == nil {
		return nil
	}
	// case 2 and case3
	if root.Val == key {
		if root.Left == nil {
			return root.Right
		}
		if root.Right == nil {
			return root.Left
		}
		suc := searchSuccessor(root)
		root.Val = suc.Val
		root.Right = deleteNode1(root.Right, suc.Val)
		return root
	}
	// search and replace the target with the successor
	if root.Val < key {
		root.Right = deleteNode1(root.Right, key)
	} else {
		root.Left = deleteNode1(root.Left, key)
	}
	return root
}

func searchSuccessor(root *TreeNode) *TreeNode {
	successor := root.Right
	for true {
		if successor.Left != nil {
			successor = successor.Left
		} else {
			break
		}
	}
	return successor
}

func main() {
	// for BST, it was too tedious to write testcases here, i did the testcases on leetcode instead
}
