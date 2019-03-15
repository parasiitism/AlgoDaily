package main

import "fmt"

/*
	2nd approach:
	- simplify and optimze the 1st approach
	- we can just save the char: last index in the hashtable
	- find the farthest reach of deletion during iteration
	- once i == farthest reach, the substring between i and previous end(this start point) is the result

	Time    O(n)
	Space   O(n)
	0 ms, faster than 100.00%
*/
func partitionLabels(S string) []int {
	// put all the keys into the ordered dict
	m := make(map[byte]int)
	for i := 0; i < len(S); i++ {
		c := S[i]
		m[c] = i
	}
	res := []int{}
	// for finding the farthest reach
	startpoint := 0
	// for recording the substring start point
	farthest := 0
	// iterate the string to record the farthest point a substring can reach
	for i := 0; i < len(S); i++ {
		c := S[i]
		if m[c] > farthest {
			farthest = m[c]
		}
		// check if the farthest == i. if yes, it means the substring btw startpoint and i is one of the result
		if i == farthest {
			res = append(res, farthest-startpoint+1)
			startpoint = i + 1
		}
	}
	return res
}

func main() {
	fmt.Println(partitionLabels("abccaddbeffe"))
}
