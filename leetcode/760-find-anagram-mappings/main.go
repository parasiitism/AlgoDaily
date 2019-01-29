package main

/*
	naive approach
	- for each word in A, search for the counter part index in B
	Time		O(n^2)
	Space		O(1)
*/

/*
	1st approach
	- hashtable
	Time		O(n)
	Space		O(n)
	0ms beats 100%
*/
func anagramMappings(A []int, B []int) []int {
	ht := make(map[int]int)
	for i := 0; i < len(B); i++ {
		ht[B[i]] = i
	}
	res := []int{}
	for i := 0; i < len(A); i++ {
		res = append(res, ht[A[i]])
	}
	return res
}

func main() {

}
