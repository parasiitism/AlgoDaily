package main

import "fmt"

/*
	questions to ask:
	- any duplicate numbers? yes
	- the numbers are not sorted? yes
*/

/*
	1st approach: hashtable, wrap 3sum with one more loop
	1. put the numbers of D in a hashtable, num:occurence as key:value
	2. for each A[i] + B[j] + C[k], find out the num from the hashtable that they sum up to zero
	3. since there are duplicate in D and we save occurence of each number in D, we can use res += m[target] to find the total count

	Time	O(n^3)
	Space	O(n)
	84 ms, faster than 15.45%
*/

func fourSumCount(A []int, B []int, C []int, D []int) int {
	m := make(map[int]int)
	for _, num := range D {
		if _, x := m[num]; !x {
			m[num] = 1
		} else {
			m[num]++
		}
	}
	res := 0
	for i := 0; i < len(A); i++ {
		for j := 0; j < len(B); j++ {
			for k := 0; k < len(C); k++ {
				temp := A[i] + B[j] + C[k]
				want := 0 - temp
				if v, x := m[want]; x {
					res += v
				}
			}
		}
	}
	return res
}

func main() {
	a := []int{1, 2}
	b := []int{-2, -1}
	c := []int{-1, 2}
	d := []int{0, 2}
	fmt.Println(fourSumCount(a, b, c, d))

	a = []int{0, 1, -1}
	b = []int{-1, 1, 0}
	c = []int{0, 0, 1}
	d = []int{-1, 1, 1}
	fmt.Println(fourSumCount(a, b, c, d))
}
