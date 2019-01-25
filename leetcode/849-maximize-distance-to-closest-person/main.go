package main

import "fmt"

/*
	1st approach
	- if close end, both ends bound with 1, e.g. 100001, the intermediate result is (zero count+1)/2
	- if open end, either one end unbound, e.g. 1000 or 0001, the intermediate result is the 'zero count'
	- find the max agmost intermediate results
	16ms beats 100%
*/
func maxDistToClosest(seats []int) int {
	zeroCnt := 0
	openEnd := false
	max := 0
	for i, seat := range seats {
		if seat == 0 {
			zeroCnt++
			if i == 0 || i == len(seats)-1 {
				openEnd = true
			}
		} else {
			if openEnd {
				if zeroCnt > max {
					max = zeroCnt
				}
			} else {
				temp := (zeroCnt + 1) / 2
				if temp > max {
					max = temp
				}
			}
			zeroCnt = 0
			openEnd = false
		}
	}
	if openEnd {
		if zeroCnt > max {
			max = zeroCnt
		}
	} else {
		temp := (zeroCnt + 1) / 2
		if temp > max {
			max = temp
		}
	}
	return max
}

func main() {
	fmt.Println(maxDistToClosest([]int{0, 1}))
	fmt.Println(maxDistToClosest([]int{1, 0}))
	fmt.Println(maxDistToClosest([]int{0, 1, 0, 1}))
	fmt.Println(maxDistToClosest([]int{1, 0, 1, 0}))

	fmt.Println(maxDistToClosest([]int{0, 0, 1, 0}))
	fmt.Println(maxDistToClosest([]int{1, 0, 0, 0}))
	fmt.Println(maxDistToClosest([]int{1, 0, 0, 1}))
	fmt.Println(maxDistToClosest([]int{1, 0, 0, 0, 1}))
}
