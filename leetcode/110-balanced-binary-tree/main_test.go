package main

import "testing"

func TestSearch(t *testing.T) {
	t.Run("", func(t *testing.T) {
		// 		5
		//	2		8
		// 1 3 7 9
		root := &TreeNode{5,
			&TreeNode{2,
				&TreeNode{1, nil, nil},
				&TreeNode{3, nil, nil},
			},
			&TreeNode{8,
				&TreeNode{7, nil, nil},
				&TreeNode{9, nil, nil},
			},
		}
		ans := isBalanced(root)
		if ans != true {
			t.Error(`fail`)
		}
	})
	t.Run("", func(t *testing.T) {
		// 		5
		//	2		8
		// 1 3
		root := &TreeNode{5,
			&TreeNode{2,
				&TreeNode{1, nil, nil},
				&TreeNode{3, nil, nil},
			},
			&TreeNode{8,
				nil,
				nil,
			},
		}
		ans := isBalanced(root)
		if ans != true {
			t.Error(`fail`)
		}
	})
	t.Run("", func(t *testing.T) {
		// 		5
		//	2
		// 1 3
		root := &TreeNode{5,
			&TreeNode{2,
				&TreeNode{1, nil, nil},
				&TreeNode{3, nil, nil},
			},
			nil,
		}
		ans := isBalanced(root)
		if ans != false {
			t.Error(`fail`, ans)
		}
	})
}
