package main

import (
	"testing"
)

func Equal(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i, v := range a {
		if v != b[i] {
			return false
		}
	}
	return true
}
func TestSearch(t *testing.T) {
	t.Run("empty arrays", func(t *testing.T) {
		ans := intersection([]int{}, []int{})
		if !Equal(ans, []int{}) {
			t.Error(`fail`)
		}
	})
	t.Run("1", func(t *testing.T) {
		ans := intersection([]int{}, []int{1})
		if !Equal(ans, []int{}) {
			t.Error(`fail`)
		}
	})
	t.Run("2", func(t *testing.T) {
		ans := intersection([]int{1}, []int{1})
		if !Equal(ans, []int{1}) {
			t.Error(`fail`)
		}
	})
	t.Run("3", func(t *testing.T) {
		ans := intersection([]int{1, 2}, []int{1})
		if !Equal(ans, []int{1}) {
			t.Error(`fail`)
		}
	})
	t.Run("4", func(t *testing.T) {
		ans := intersection([]int{1, 2}, []int{1, 2})
		if !Equal(ans, []int{1, 2}) {
			t.Error(`fail`)
		}
	})
	t.Run("5", func(t *testing.T) {
		ans := intersection([]int{1, 2}, []int{3})
		if !Equal(ans, []int{}) {
			t.Error(`fail`)
		}
	})
	t.Run("6", func(t *testing.T) {
		ans := intersection([]int{1, 2, 3, 5}, []int{-1, 2, 3, 4})
		if !Equal(ans, []int{2, 3}) {
			t.Error(`fail`)
		}
	})
	t.Run("6", func(t *testing.T) {
		ans := intersection([]int{1, 2, 2, 1, 1}, []int{2, 2, 3, 3})
		if !Equal(ans, []int{2}) {
			t.Error(`fail`)
		}
	})
	t.Run("6", func(t *testing.T) {
		ans := intersection([]int{1, 2, 2, 2, 1, 1, 3}, []int{2, 2, 3, 3})
		if !Equal(ans, []int{2, 3}) {
			t.Error(`fail`)
		}
	})
}
