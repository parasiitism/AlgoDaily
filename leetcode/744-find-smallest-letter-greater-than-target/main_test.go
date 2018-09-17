package main

import "testing"

func TestSearch(t *testing.T) {
	t.Run("2 items array", func(t *testing.T) {
		arr := []byte{'b', 'c'}
		ans := nextGreatestLetter(arr, 'a')
		if ans != 'b' {
			t.Error(`fail`)
		}
	})
	t.Run("2 items array", func(t *testing.T) {
		arr := []byte{'b', 'c'}
		ans := nextGreatestLetter(arr, 'b')
		if ans != 'c' {
			t.Error(`fail`)
		}
	})
	t.Run("2 items array", func(t *testing.T) {
		arr := []byte{'b', 'c'}
		ans := nextGreatestLetter(arr, 'c')
		if ans != 'b' {
			t.Error(`fail`)
		}
	})
	t.Run("3 items array", func(t *testing.T) {
		arr := []byte{'c', 'f', 'j'}
		ans := nextGreatestLetter(arr, 'a')
		if ans != 'c' {
			t.Error(`fail`)
		}
	})
	t.Run("3 items array", func(t *testing.T) {
		arr := []byte{'c', 'f', 'j'}
		ans := nextGreatestLetter(arr, 'c')
		if ans != 'f' {
			t.Error(`fail`)
		}
	})
	t.Run("3 items array", func(t *testing.T) {
		arr := []byte{'c', 'f', 'j'}
		ans := nextGreatestLetter(arr, 'd')
		if ans != 'f' {
			t.Error(`fail`)
		}
	})
	t.Run("3 items array", func(t *testing.T) {
		arr := []byte{'c', 'f', 'j'}
		ans := nextGreatestLetter(arr, 'g')
		if ans != 'j' {
			t.Error(`fail`)
		}
	})
	t.Run("3 items array", func(t *testing.T) {
		arr := []byte{'c', 'f', 'j'}
		ans := nextGreatestLetter(arr, 'j')
		if ans != 'c' {
			t.Error(`fail`)
		}
	})
	t.Run("3 items array", func(t *testing.T) {
		arr := []byte{'c', 'f', 'j'}
		ans := nextGreatestLetter(arr, 'k')
		if ans != 'c' {
			t.Error(`fail`)
		}
	})
	t.Run("duplicate items array", func(t *testing.T) {
		arr := []byte{'c', 'c', 'f', 'j'}
		ans := nextGreatestLetter(arr, 'c')
		if ans != 'f' {
			t.Error(`fail`)
		}
	})
}
