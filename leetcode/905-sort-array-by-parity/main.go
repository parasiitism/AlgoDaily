package main

/*
	1st approach
	- x%2
	72ms beats 100%
*/
func sortArrayByParity(A []int) []int {
	even := []int{}
	odd := []int{}
	for _, a := range A {
		if a%2 == 0 {
			even = append(even, a)
		} else {
			odd = append(odd, a)
		}
	}
	even = append(even, odd...)
	return even
}

func main() {

}
