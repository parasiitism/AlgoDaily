package main

import "testing"

func TestSearch(t *testing.T) {

	// init

	var nums []int
	var target int
	var ans int

	// cases

	t.Run("empty array", func(t *testing.T) {
		nums = []int{}
		target = 10
		ans = search(nums, target)
		if ans != -1 {
			t.Error(`fail`)
		}
	})

	t.Run("single item array", func(t *testing.T) {
		nums = []int{10}
		t.Run("exists", func(t *testing.T) {
			target = 10
			ans = search(nums, target)
			if ans != 0 {
				t.Error(`fail`)
			}
		})

		t.Run("left not exist", func(t *testing.T) {
			target = 1
			ans = search(nums, target)
			if ans != -1 {
				t.Error(`fail`)
			}
		})

		t.Run("right not exist", func(t *testing.T) {
			target = 20
			ans = search(nums, target)
			if ans != -1 {
				t.Error(`fail`)
			}
		})
	})

	t.Run("2 items array", func(t *testing.T) {
		nums = []int{10, 20}
		t.Run("left", func(t *testing.T) {
			target = 10
			ans = search(nums, target)
			if ans != 0 {
				t.Error(`fail`)
			}
		})

		t.Run("right", func(t *testing.T) {
			target = 20
			ans = search(nums, target)
			if ans != 1 {
				t.Error(`fail`)
			}
		})

		t.Run("left not exist", func(t *testing.T) {
			target = 1
			ans = search(nums, target)
			if ans != -1 {
				t.Error(`fail`)
			}
		})

		t.Run("right not exist", func(t *testing.T) {
			target = 30
			ans = search(nums, target)
			if ans != -1 {
				t.Error(`fail`)
			}
		})
	})

	t.Run("3 items array", func(t *testing.T) {
		nums = []int{10, 20, 30}
		t.Run("left", func(t *testing.T) {
			target = 10
			ans = search(nums, target)
			if ans != 0 {
				t.Error(`fail`)
			}
		})

		t.Run("middle", func(t *testing.T) {
			target = 20
			ans = search(nums, target)
			if ans != 1 {
				t.Error(`fail`)
			}
		})

		t.Run("right", func(t *testing.T) {
			target = 30
			ans = search(nums, target)
			if ans != 2 {
				t.Error(`fail`)
			}
		})

		t.Run("left not exist", func(t *testing.T) {
			target = 1
			ans = search(nums, target)
			if ans != -1 {
				t.Error(`fail`)
			}
		})

		t.Run("right not exist", func(t *testing.T) {
			target = 40
			ans = search(nums, target)
			if ans != -1 {
				t.Error(`fail`)
			}
		})
	})

	t.Run("whatever array", func(t *testing.T) {
		nums = []int{1, 3, 6, 7, 9, 10}
		target = 9
		ans = search(nums, target)
		if ans != 4 {
			t.Error(`fail`)
		}
	})

	// dont test large data set for now
}
