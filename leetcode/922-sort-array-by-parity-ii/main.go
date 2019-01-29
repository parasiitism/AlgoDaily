package main

/*
	1st approach
	- split the array by parity
	- put the even array and odd array items into the result intermittently
*/
func sortArrayByParityII(A []int) []int {
	even := []int{}
	odd := []int{}
	for _, a := range A {
		if a%2 == 0 {
			even = append(even, a)
		} else {
			odd = append(odd, a)
		}
	}
	res := []int{}
	for i := 0; i < len(even); i++ {
		res = append(res, even[i])
		res = append(res, odd[i])
	}
	return even
}

func main() {

}
