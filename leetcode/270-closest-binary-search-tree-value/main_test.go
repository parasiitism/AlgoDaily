package main

import "testing"

func TestSearch(t *testing.T) {
	t.Run("", func(t *testing.T) {
		root := &TreeNode{4,
			&TreeNode{2,
				&TreeNode{1, nil, nil},
				&TreeNode{3, nil, nil},
			},
			&TreeNode{5, nil, nil},
		}
		ans := closestValue(root, 2.1)
		if ans != 2 {
			t.Error(`fail`)
		}
	})

	t.Run("", func(t *testing.T) {
		root := &TreeNode{4,
			&TreeNode{2,
				&TreeNode{1, nil, nil},
				nil,
			},
			&TreeNode{5, nil, nil},
		}
		ans := dfs(root, 1.1)
		if ans != 1 {
			t.Error(`fail`)
		}
	})

	t.Run("", func(t *testing.T) {
		root := &TreeNode{15,
			&TreeNode{14, nil, nil},
			nil,
		}
		ans := dfs(root, -14)
		if ans != 14 {
			t.Error(`fail`)
		}
	})
}
