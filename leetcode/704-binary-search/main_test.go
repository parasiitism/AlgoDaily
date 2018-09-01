package main

import "testing"

func TestSearch(t *testing.T) {
	nums := []int{1, 3, 5}
	target := 10
	ans := search(nums, target)
	if ans != -1 {
		t.Error(`fail`)
	}
}
