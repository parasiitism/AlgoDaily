package main

import "testing"

func TestSearch(t *testing.T) {

	t.Run("0", func(t *testing.T) {
		ans := mySqrt2(0)
		if ans != 0 {
			t.Error(`fail`)
		}
	})

	t.Run("1", func(t *testing.T) {
		ans := mySqrt2(1)
		if ans != 1 {
			t.Error(`fail`)
		}
	})

	t.Run("2", func(t *testing.T) {
		ans := mySqrt2(2)
		if ans != 1 {
			t.Error(`fail`)
		}
	})

	t.Run("3", func(t *testing.T) {
		ans := mySqrt2(3)
		if ans != 1 {
			t.Error(`fail`)
		}
	})

	t.Run("4", func(t *testing.T) {
		ans := mySqrt2(4)
		if ans != 2 {
			t.Error(`fail`)
		}
	})

	t.Run("8", func(t *testing.T) {
		ans := mySqrt2(8)
		if ans != 2 {
			t.Error(`fail`)
		}
	})

	t.Run("10", func(t *testing.T) {
		ans := mySqrt2(10)
		if ans != 3 {
			t.Error(`fail`)
		}
	})

	t.Run("100", func(t *testing.T) {
		ans := mySqrt2(100)
		if ans != 10 {
			t.Error(`fail`)
		}
	})

	t.Run("101", func(t *testing.T) {
		ans := mySqrt2(101)
		if ans != 10 {
			t.Error(`fail`)
		}
	})

	t.Run("120", func(t *testing.T) {
		ans := mySqrt2(120)
		if ans != 10 {
			t.Error(`fail`)
		}
	})

	t.Run("121", func(t *testing.T) {
		ans := mySqrt2(121)
		if ans != 11 {
			t.Error(`fail`)
		}
	})
}
