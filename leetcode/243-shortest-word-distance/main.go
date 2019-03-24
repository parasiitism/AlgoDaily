package main

import "fmt"

/*
	questions to ask:
  - will word1 == word2?
  - will either word1, word2 be in the list always?
*/

/*
	1st approach: 2 pointers

	Time    O(n)
	Space   O(1)
	4ms beats 100%
*/
func shortestDistance(words []string, word1 string, word2 string) int {
	p1 := -1
	p2 := -1
	res := len(words)
	for i := 0; i < len(words); i++ {
		word := words[i]
		if word == word1 {
			p1 = i
		}
		if word == word2 {
			p2 = i
		}
		diff := abs(p1 - p2)
		if p1 != -1 && p2 != -1 && diff < res {
			res = diff
		}
	}
	return res
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

/*
	1st approach: binary search the nearest target index

	Time    O(mlogn) m: word1, n: word2
	Space   O(m+n)
	12 ms, faster than 7.14%
*/
func shortestDistance1(words []string, word1 string, word2 string) int {
	m := make(map[string][]int)
	for i := 0; i < len(words); i++ {
		word := words[i]
		if _, x := m[word]; !x {
			m[word] = []int{i}
		} else {
			m[word] = append(m[word], i)
		}
	}
	arr1 := m[word1]
	arr2 := m[word2]
	res := len(words)
	// binary search
	for _, targetIdx := range arr1 {
		left := 0
		right := len(arr2) - 1
		for left <= right {
			mid := (left + right) / 2
			// compare with the result
			diff := abs(targetIdx - arr2[mid])
			if diff < res {
				res = diff
			}
			// binary search range narrowing
			if arr2[mid] < targetIdx {
				left = mid + 1
			} else {
				right = mid - 1
			}
		}
	}
	return res
}

func main() {
	a := []string{"practice", "makes", "perfect", "coding", "makes"}
	fmt.Println(shortestDistance1(a, "coding", "practice"))

	a = []string{"practice", "makes", "perfect", "coding", "makes"}
	fmt.Println(shortestDistance1(a, "coding", "makes"))
}
