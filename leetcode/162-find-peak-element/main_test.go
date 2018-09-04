package main

import "testing"

func TestSearch(t *testing.T) {

	t.Run("empty array", func(t *testing.T) {
		ans := findPeakElement([]int{})
		if ans != -1 {
			t.Error(`fail`)
		}
	})

	t.Run("single item array", func(t *testing.T) {
		ans := findPeakElement([]int{2})
		if ans != 0 {
			t.Error(`fail`)
		}
	})

	t.Run("2 items array", func(t *testing.T) {

		t.Run("left", func(t *testing.T) {
			ans := findPeakElement([]int{1, 2})
			if ans != 1 {
				t.Error(`fail`)
			}
		})

		t.Run("right", func(t *testing.T) {
			ans := findPeakElement([]int{2, 1})
			if ans != 0 {
				t.Error(`fail`)
			}
		})

	})

	t.Run("3 items array", func(t *testing.T) {

		t.Run("left", func(t *testing.T) {
			ans := findPeakElement([]int{2, 1, 1})
			if ans != 0 {
				t.Error(`fail`)
			}
		})

		t.Run("mid", func(t *testing.T) {
			ans := findPeakElement([]int{1, 2, 1})
			if ans != 1 {
				t.Error(`fail`)
			}
		})

		t.Run("right", func(t *testing.T) {
			ans := findPeakElement([]int{1, 1, 2})
			if ans != 2 {
				t.Error(`fail`)
			}
		})

	})

	t.Run("3 items array", func(t *testing.T) {

		t.Run("left", func(t *testing.T) {
			ans := findPeakElement([]int{1, 2, 3, 1})
			if ans != 2 {
				t.Error(`fail`)
			}
		})
	})

	t.Run("larger", func(t *testing.T) {

		t.Run("left", func(t *testing.T) {
			ans := findPeakElement([]int{1, 2, 1, 3, 5, 6, 4})
			if ans != 1 {
				t.Error(`fail`)
			}
		})
	})

}
