package main

import (
	"fmt"
)

// search for the upper bound and the target is simply the target_idx+1 item
// e.g.
// arr=abcccd, target=c => upperbound = arr[4] so ans = arr[5]
func upper(arr []byte, target byte) int {
	min := 0
	max := len(arr) - 1
	for min < max {
		mean := (min + max + 1) / 2
		if target >= arr[mean] {
			min = mean
		} else {
			max = mean - 1
		}
	}
	return min
}

func nextGreatestLetter(letters []byte, target byte) byte {
	x := upper(letters, target)
	if target >= letters[x] {
		if x == len(letters)-1 {
			return letters[0]
		}
		return letters[x+1]
	}
	return letters[x]
}

func main() {
	// x := upper([]byte{'b', 'd', 'd', 'e'}, 'd')
	// fmt.Println(x)
	// x = upper([]byte{'b', 'd', 'd', 'e'}, 'c')
	// fmt.Println(x)
	x := nextGreatestLetter([]byte{'b', 'd', 'e'}, 'c')
	fmt.Println(x)
}
