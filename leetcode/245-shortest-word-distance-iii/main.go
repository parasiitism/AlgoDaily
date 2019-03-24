package main

/*
	1st approach: binary search the nearest target index

	Time    worst O(mlogn) m: word1, n: word2
	Time    best O(n) when word1==word2
	Space   O(m+n)
	ms, faster than 37.50%
*/
func shortestWordDistance(words []string, word1 string, word2 string) int {
	m := make(map[string][]int)
	for i := 0; i < len(words); i++ {
		word := words[i]
		if _, x := m[word]; !x {
			m[word] = []int{i}
		} else {
			m[word] = append(m[word], i)
		}
	}
	if word1 == word2 {
		res := len(words)
		arr := m[word1]
		for i := 1; i < len(arr); i++ {
			diff := arr[i] - arr[i-1]
			if diff < res {
				res = diff
			}
		}
		return res
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

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

/*
	2nd approach: 2 pointers

	Time    O(n)
	Space   O(m+n)
	4 ms, faster than 100.00%
*/
func shortestWordDistance1(words []string, word1 string, word2 string) int {
	p1 := -1
	p2 := -1
	res := len(words)
	for i := 0; i < len(words); i++ {
		word := words[i]
		if word1 == word2 {
			if word == word1 {
				if p1 == -1 {
					p1 = i
				} else {
					diff := i - p1
					p1 = i
					if diff < res {
						res = diff
					}
				}
			}
		} else {
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
	}
	return res
}

func main() {

}
