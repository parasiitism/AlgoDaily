package main

import "fmt"

/*
	1st approach
	- use array of set(hashtables)
	- if a and b are not in the same hashtable, combine hashtables
	- if a is found but b is not, add b to the hashtable which has a
	- if b is found but a is not, add a to the hashtable which has b
	- if a and b are not found, create a new hashtable for them
	Time		O(n*m) m depends on the distribution of the nunmbers(numbers of hashtables)
	Space		O(n) although we have many hashtables, the nodes are unique, the hashtables actually store at most the number of nodes
	40ms beats 100%
*/
func countComponents(n int, edges [][]int) int {
	hashtables := []map[int]bool{}
	for _, edge := range edges {
		a := edge[0]
		b := edge[1]

		aClusterIdx := -1
		bClusterIdx := -1

		for i := 0; i < len(hashtables); i++ {
			ht := hashtables[i]
			if _, x := ht[a]; x {
				aClusterIdx = i
				break
			}
		}

		for i := 0; i < len(hashtables); i++ {
			ht := hashtables[i]
			if _, x := ht[b]; x {
				bClusterIdx = i
				break
			}
		}

		if aClusterIdx > -1 && bClusterIdx > -1 {
			if aClusterIdx == bClusterIdx {
				continue
			}
			hta := hashtables[aClusterIdx]
			for k, v := range hashtables[bClusterIdx] {
				hta[k] = v
			}
			hashtables = append(hashtables[:bClusterIdx], hashtables[bClusterIdx+1:]...)
		} else if aClusterIdx > -1 {
			hta := hashtables[aClusterIdx]
			hta[b] = true
		} else if bClusterIdx > -1 {
			htb := hashtables[bClusterIdx]
			htb[a] = true
		} else {
			ht := make(map[int]bool)
			ht[a] = true
			ht[b] = true
			hashtables = append(hashtables, ht)
		}

	}
	// count the numbers which are not contained in edges
	miss := 0
	for i := 0; i < n; i++ {
		found := false
		for _, ht := range hashtables {
			if _, x := ht[i]; x {
				found = true
				break
			}
		}
		if found == false {
			miss++
		}
	}
	return len(hashtables) + miss
}

func main() {
	a := [][]int{
		{0, 1}, {1, 2}, {3, 4},
	}
	fmt.Println(countComponents(5, a))

	a = [][]int{
		{0, 1}, {1, 2}, {2, 3}, {3, 4},
	}
	fmt.Println(countComponents(5, a))

	a = [][]int{
		{2, 3}, {1, 2}, {1, 3},
	}
	fmt.Println(countComponents(4, a))
}
