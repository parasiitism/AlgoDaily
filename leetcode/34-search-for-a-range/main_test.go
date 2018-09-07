package main

import (
	"fmt"
	"testing"
)

func TestSearch(t *testing.T) {

	t.Run("[]", func(t *testing.T) {
		a := []int{}
		ans := searchRange(a, 3)
		if ans[0] != -1 {
			t.Error(`fail`)
		} else {
			fmt.Println("[] ✅")
		}
	})

	t.Run("[1] 1", func(t *testing.T) {
		a := []int{1}
		ans := searchRange(a, 1)
		if ans[0] != 0 && ans[1] != 0 {
			t.Error(`fail`)
		} else {
			fmt.Println("[1] 1 ✅")
		}
	})
	t.Run("[1] 3", func(t *testing.T) {
		a := []int{1}
		ans := searchRange(a, 3)
		if ans[0] != -1 {
			t.Error(`fail`)
		} else {
			fmt.Println("[1] 3 ✅")
		}
	})

	t.Run("[1,2] 3", func(t *testing.T) {
		a := []int{1, 2}
		ans := searchRange(a, 3)
		if ans[0] != -1 {
			t.Error(`fail`)
		} else {
			fmt.Println("[1,2] 3 ✅")
		}
	})
	t.Run("[1,2] 1", func(t *testing.T) {
		a := []int{1, 2}
		ans := searchRange(a, 1)
		if ans[0] != 0 {
			t.Error(`fail`)
		} else {
			fmt.Println("[1,2] 1 ✅")
		}
	})
	t.Run("[1,2] 2", func(t *testing.T) {
		a := []int{1, 2}
		ans := searchRange(a, 2)
		if ans[0] != 1 && ans[1] != 1 {
			t.Error(`fail`)
		} else {
			fmt.Println("[1,2] 2 ✅")
		}
	})

	t.Run("[1,2,2] 3", func(t *testing.T) {
		a := []int{1, 2, 2}
		ans := searchRange(a, 3)
		if ans[0] != -1 {
			t.Error(`fail`)
		} else {
			fmt.Println("[1,2,2] 3 ✅")
		}
	})
	t.Run("[1,2,2] 1", func(t *testing.T) {
		a := []int{1, 2, 2}
		ans := searchRange(a, 1)
		if ans[0] != 0 && ans[1] != 0 {
			t.Error(`fail`)
		} else {
			fmt.Println("[1,2,2] 1 ✅")
		}
	})
	t.Run("[1,2,2] 2", func(t *testing.T) {
		a := []int{1, 2, 2}
		ans := searchRange(a, 2)
		fmt.Println("fukc", ans)
		if ans[0] != 1 && ans[1] != 2 {
			t.Error(`fail`)
		} else {
			fmt.Println("[1,2,2] 2 ✅")
		}
	})

	t.Run("[1,1,2] 3", func(t *testing.T) {
		a := []int{1, 2, 2}
		ans := searchRange(a, 3)
		fmt.Println("fukc", ans)
		if ans[0] != -1 {
			t.Error(`fail`)
		} else {
			fmt.Println("[1,1,2] 3 ✅")
		}
	})
	t.Run("[1,1,2] 2", func(t *testing.T) {
		a := []int{1, 2, 2}
		ans := searchRange(a, 2)
		fmt.Println("fukc", ans)
		if ans[0] != 2 && ans[1] != 2 {
			t.Error(`fail`)
		} else {
			fmt.Println("[1,2,2] 2 ✅")
		}
	})
	t.Run("[1,1,2] 1", func(t *testing.T) {
		a := []int{1, 2, 2}
		ans := searchRange(a, 1)
		fmt.Println("fukc", ans)
		if ans[0] != 0 && ans[1] != 0 {
			t.Error(`fail`)
		} else {
			fmt.Println("[1,2,2] 2 ✅")
		}
	})
}
