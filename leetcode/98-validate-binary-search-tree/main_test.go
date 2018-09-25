package main

import (
	"math"
	"testing"
)

func TestSearch(t *testing.T) {

	var root *TreeNode
	var ans bool

	t.Run("0", func(t *testing.T) {
		ans = isValidBST(root)
		if ans != true {
			t.Error(`fail`)
		}
	})

	t.Run("0", func(t *testing.T) {
		// 		1
		//	2		3
		root = &TreeNode{1,
			&TreeNode{2, nil, nil},
			&TreeNode{3, nil, nil},
		}

		ans = isValidBST(root)
		if ans != false {
			t.Error(`fail`)
		}
	})

	t.Run("0", func(t *testing.T) {
		// 		2
		//	1		3
		root = &TreeNode{2,
			&TreeNode{1, nil, nil},
			&TreeNode{3, nil, nil},
		}

		ans = isValidBST(root)
		if ans != true {
			t.Error(`fail`)
		}
	})

	t.Run("0", func(t *testing.T) {
		// 			2
		//		1		3
		// -1
		root = &TreeNode{
			2,
			&TreeNode{
				1,
				&TreeNode{
					-1,
					nil,
					nil,
				},
				nil},
			&TreeNode{3, nil, nil},
		}
		ans = isValidBST(root)
		if ans != true {
			t.Error(`fail`)
		}
	})

	t.Run("0", func(t *testing.T) {
		// 			2
		//		1		3
		// 0	 2
		root = &TreeNode{2,
			&TreeNode{1,
				&TreeNode{0,
					nil,
					nil,
				},
				&TreeNode{2,
					nil,
					nil,
				},
			},
			&TreeNode{3, nil, nil},
		}
		ans = isValidBST(root)
		if ans != false {
			t.Error(`fail`)
		}
	})

	t.Run("0", func(t *testing.T) {
		// 			min
		//		nil		max
		root = &TreeNode{math.MinInt64,
			nil,
			&TreeNode{math.MaxInt64, nil, nil},
		}
		ans = isValidBST(root)
		if ans != true {
			t.Error(`fail`)
		}
	})
}
