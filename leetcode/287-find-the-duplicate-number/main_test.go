package main

import (
	"testing"
)

func TestSearch(t *testing.T) {
	t.Run("empty array", func(t *testing.T) {
		ans := findDuplicate([]int{})
		if ans != -1 {
			t.Error(`fail`)
		}
	})
	t.Run("1 item array", func(t *testing.T) {
		ans := findDuplicate([]int{1})
		if ans != -1 {
			t.Error(`fail`)
		}
	})
	t.Run("2", func(t *testing.T) {
		ans := findDuplicate([]int{1, 1})
		if ans != 1 {
			t.Error(`fail`)
		}
	})
	t.Run("3", func(t *testing.T) {
		ans := findDuplicate([]int{1, 1, 1})
		if ans != 1 {
			t.Error(`fail`)
		}
	})
	t.Run("4", func(t *testing.T) {
		ans := findDuplicate([]int{1, 1, 1, 2})
		if ans != 1 {
			t.Error(`fail`)
		}
	})
}
