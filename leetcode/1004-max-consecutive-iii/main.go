package main

import "fmt"

/*
	1st approach:
	1. make [1,0,1,1,0] to [1,0,2,0]
	2. for each num, count the sum to the front at most flipping k zeros
	3. compare the cur with the intermediate result

	Time	O(n^2)
	Space	O(n)
	788 ms, faster than 11.11%
*/
func longestOnes(A []int, K int) int {
	// make [1,0,1,1,0] to [1,0,2,0]
	arr := []int{}
	count := 0
	for i := 0; i < len(A); i++ {
		if A[i] == 1 {
			count++
			if i+1 == len(A) {
				arr = append(arr, count)
			}
		} else {
			if count > 0 {
				arr = append(arr, count)
			}
			count = 0
			// append the current 0
			arr = append(arr, 0)
		}
	}
	// if all 1
	if count == len(A) {
		return count
	}
	// count
	// [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
	// becomes [0 0 2 0 0 3 0 2 0 0 0 4]
	// for each num, count the sum if flip k of 0->1
	res := 0
	for i := 0; i < len(arr); i++ {
		cur := 0
		zeroCnt := 0
		j := i
		for zeroCnt <= K && j >= 0 {
			if arr[j] == 0 {
				// if 0, flip 0 to 1 therefore zeroCnt++
				if zeroCnt < K {
					cur++
				}
				// consume quota
				zeroCnt++
			} else {
				// if > 0, add to sum
				cur += arr[j]
			}
			j--
		}
		// compare the current sum and the result sum
		if cur > res {
			res = cur
		}
	}
	return res
}

func main() {
	fmt.Println(longestOnes([]int{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0}, 2))
	fmt.Println(longestOnes([]int{0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1}, 3))

	fmt.Println(longestOnes([]int{1, 0, 1, 1, 0}, 2))
	fmt.Println(longestOnes([]int{1, 0, 1, 1, 1}, 2))
	fmt.Println(longestOnes([]int{1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1}, 2))

	fmt.Println(longestOnes([]int{1}, 2))
	fmt.Println(longestOnes([]int{1, 1, 1}, 2))
}
