package main

import "fmt"

/*
	1st approach
	- 2 pointers to indicate the start and the end(use an array to store all the indexes)
	- hashtable to store the characters frequency

	Time    O(n)
  Space   O(n)
	308ms beats 20.83%
	5feb2019
*/
func minWindow(s string, t string) string {
	indexes := []int{}
	minimum := s
	// give me the 'structure' of the target string
	targetStructure := make(map[byte]int)
	for i := 0; i < len(t); i++ {
		c := t[i]
		if _, x := targetStructure[c]; x {
			targetStructure[c]++
		} else {
			targetStructure[c] = 1
		}
	}
	// construct for finding the the start and the end
	curStructure := make(map[byte]int)
	for k := range targetStructure {
		curStructure[k] = 0
	}
	// iterate the s
	for i := 0; i < len(s); i++ {
		c := s[i]
		if _, x := targetStructure[c]; !x {
			continue
		}
		indexes = append(indexes, i)
		curStructure[c]++
		for checkSameStructure(targetStructure, curStructure) {
			end := indexes[len(indexes)-1]
			start := indexes[0]
			length := end - start + 1
			if length < len(minimum) {
				minimum = s[start : end+1]
			}
			popped := indexes[0]
			indexes = indexes[1:]
			curStructure[s[popped]]--
		}
	}
	// if unfortunately the lengths are the same
	if len(minimum) == len(s) {
		// clear the construct
		curStructure = make(map[byte]int)
		for key := range targetStructure {
			curStructure[key] = 0
		}
		for i := 0; i < len(s); i++ {
			c := s[i]
			if _, x := targetStructure[c]; x {
				curStructure[c]++
			}
		}
		if checkSameStructure(targetStructure, curStructure) {
			return s
		}
		return ""
	}

	return minimum
}

func checkSameStructure(a, b map[byte]int) bool {
	for key := range a {
		if _, x := b[key]; !x {
			return false
		} else if a[key] > b[key] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(minWindow("ADOBECODEBANC", "ABC"))
	fmt.Println(minWindow("ADOBECODEBANC", "ABCB"))
	fmt.Println(minWindow("ADOBECODEBANCBABB", "ABC"))
	fmt.Println(minWindow("ADOBBECCOBDEBANC", "ABC"))
	fmt.Println(minWindow("ADOBECODEBANC", "ABc"))
}
