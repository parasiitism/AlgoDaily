package main

import "testing"

func TestSearch(t *testing.T) {

	t.Run("0", func(t *testing.T) {
		nums := []int{4, 5, 6, 7, 0, 1, 2}
		target := 4
		ans := search(nums, target)
		if ans != 0 {
			t.Error(`fail`)
		}
	})

	t.Run("0", func(t *testing.T) {
		nums := []int{4, 5, 6, 7, 0, 1, 2}
		target := 5
		ans := search(nums, target)
		if ans != 1 {
			t.Error(`fail`)
		}
	})

	t.Run("0", func(t *testing.T) {
		nums := []int{4, 5, 6, 7, 0, 1, 2}
		target := 6
		ans := search(nums, target)
		if ans != 2 {
			t.Error(`fail`)
		}
	})

	t.Run("0", func(t *testing.T) {
		nums := []int{4, 5, 6, 7, 0, 1, 2}
		target := 7
		ans := search(nums, target)
		if ans != 3 {
			t.Error(`fail`)
		}
	})

	t.Run("0", func(t *testing.T) {
		nums := []int{4, 5, 6, 7, 0, 1, 2}
		target := 0
		ans := search(nums, target)
		if ans != 4 {
			t.Error(`fail`)
		}
	})

	t.Run("0", func(t *testing.T) {
		nums := []int{4, 5, 6, 7, 0, 1, 2}
		target := 2
		ans := search(nums, target)
		if ans != 6 {
			t.Error(`fail`)
		}
	})

	t.Run("1", func(t *testing.T) {
		nums := []int{4, 5, 6, 7, 8, 1, 2, 3}
		target := 7
		ans := search(nums, target)
		if ans != 3 {
			t.Error(`fail`)
		}
	})

	t.Run("1", func(t *testing.T) {
		nums := []int{4, 5, 6, 7, 8, 1, 2, 3}
		target := 8
		ans := search(nums, target)
		if ans != 4 {
			t.Error(`fail`)
		}
	})

	t.Run("1", func(t *testing.T) {
		nums := []int{4, 5, 6, 7, 8, 1, 2, 3}
		target := 1
		ans := search(nums, target)
		if ans != 5 {
			t.Error(`fail`)
		}
	})

	t.Run("1", func(t *testing.T) {
		nums := []int{}
		target := 1
		ans := search(nums, target)
		if ans != -1 {
			t.Error(`fail`)
		}
	})

	t.Run("1", func(t *testing.T) {
		nums := []int{5, 1}
		target := 5
		ans := search(nums, target)
		if ans != 0 {
			t.Error(`fail`)
		}
	})

	t.Run("1", func(t *testing.T) {
		nums := []int{5, 1}
		target := 1
		ans := search(nums, target)
		if ans != 1 {
			t.Error(`fail`)
		}
	})

	t.Run("1", func(t *testing.T) {
		nums := []int{1, 5}
		target := 1
		ans := search(nums, target)
		if ans != 0 {
			t.Error(`fail`)
		}
	})

	t.Run("1", func(t *testing.T) {
		nums := []int{1, 5}
		target := 5
		ans := search(nums, target)
		if ans != 1 {
			t.Error(`fail`)
		}
	})

}
