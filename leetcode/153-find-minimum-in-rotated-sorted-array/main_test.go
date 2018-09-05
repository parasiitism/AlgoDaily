package main

import "testing"

func TestSearch(t *testing.T) {
	t.Run("single item array", func(t *testing.T) {
		ans := findMin([]int{2})
		if ans != 2 {
			t.Error(`fail`)
		}
	})
	t.Run("2 items array", func(t *testing.T) {
		ans := findMin([]int{2, 1})
		if ans != 1 {
			t.Error(`fail`)
		}
	})
	t.Run("3 items array", func(t *testing.T) {
		ans := findMin([]int{1, 2, 0})
		if ans != 0 {
			t.Error(`fail`)
		}
	})
	t.Run("3 items array", func(t *testing.T) {
		ans := findMin([]int{4, 5, 6, 7, 0, 1, 2})
		if ans != 0 {
			t.Error(`fail`)
		}
	})
}
