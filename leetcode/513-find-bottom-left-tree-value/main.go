package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach: bfs
	- bfs
	- the result is the 1st item in the bottom layer of the tree
	12ms beats 100%
	14jan2019
*/
func findBottomLeftValue(root *TreeNode) int {
	bottomLeft := root.Val
	q := []*TreeNode{}
	q = append(q, root)
	for len(q) > 0 {
		layerSize := len(q)
		for i := 0; i < layerSize; i++ {
			head := q[0]
			q = q[1:]
			if i == 0 {
				bottomLeft = head.Val
			}
			if head.Left != nil {
				q = append(q, head.Left)
			}
			if head.Right != nil {
				q = append(q, head.Right)
			}
		}
	}
	return bottomLeft
}

func main() {
	// 			7
	//		3		11
	// 0	 6 8  15
	root := &TreeNode{7,
		&TreeNode{3,
			&TreeNode{0,
				nil,
				nil,
			},
			&TreeNode{6,
				nil,
				nil,
			},
		},
		&TreeNode{11,
			&TreeNode{8,
				nil,
				nil,
			},
			&TreeNode{15,
				nil,
				nil,
			},
		},
	}
	fmt.Println(findBottomLeftValue(root))
	// 			7
	//		3		11
	// 0	 6 8  15
	//		5
	root = &TreeNode{7,
		&TreeNode{3,
			&TreeNode{0,
				nil,
				nil,
			},
			&TreeNode{6,
				&TreeNode{5,
					nil,
					nil,
				},
				nil,
			},
		},
		&TreeNode{11,
			&TreeNode{8,
				nil,
				nil,
			},
			&TreeNode{15,
				nil,
				nil,
			},
		},
	}
	fmt.Println(findBottomLeftValue(root))
}
